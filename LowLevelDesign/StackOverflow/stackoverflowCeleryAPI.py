from enum import Enum
from threading import Lock
import uuid
from datetime import datetime
import redis
from sqlalchemy import create_engine, Column, String, Integer, Text, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy.exc import IntegrityError
from fastapi import FastAPI, HTTPException, UploadFile, File, Form, Query
from celery import Celery

# Initialize database engine
db_engine = create_engine("postgresql://postgres:password@localhost/stack_overflow")
Session = sessionmaker(bind=db_engine)
session = Session()
Base = declarative_base()

# Initialize Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Initialize FastAPI
app = FastAPI()

# Initialize Celery
celery_app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

# Enum for Vote Type
class VoteType(Enum):
    UPVOTE = 1
    DOWNVOTE = -1

# Database Models
class Question(Base):
    __tablename__ = 'questions'
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    tags = Column(String, nullable=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    votes = Column(Integer, default=0)
    answers = relationship("Answer", back_populates="question")

class Answer(Base):
    __tablename__ = 'answers'
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    content = Column(Text, nullable=False)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    question_id = Column(String, ForeignKey("questions.id"), nullable=False)
    votes = Column(Integer, default=0)
    question = relationship("Question", back_populates="answers")

class User(Base):
    __tablename__ = 'users'
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    username = Column(String, unique=True, nullable=False)
    reputation = Column(Integer, default=0)

# Create Tables
Base.metadata.create_all(db_engine)

# Celery Task for Background Vote Syncing
@celery_app.task
def sync_votes_to_db():
    """Background task to periodically sync vote counts from Redis to the database."""
    questions = session.query(Question).all()
    for question in questions:
        votes = int(r.get(f"question:{question.id}:votes") or 0)
        question.votes = votes
    session.commit()

# API Endpoints
@app.post("/questions/")
def create_question(
    title: str = Form(...), 
    content: str = Form(...), 
    tags: str = Form(...), 
    username: str = Form(...), 
    file: UploadFile = File(None)
):
    user = session.query(User).filter_by(username=username).first()
    if not user:
        user = User(username=username)
        session.add(user)
        session.commit()
    
    question = Question(title=title, content=content, tags=tags, user_id=user.id)
    session.add(question)
    session.commit()
    
    # Store question votes in Redis
    r.set(f"question:{question.id}:votes", 0)
    
    if file:
        file_location = f"uploads/{file.filename}"
        with open(file_location, "wb") as f:
            f.write(file.file.read())
        return {"question_id": question.id, "message": "Question posted successfully with file upload", "file": file_location}
    
    return {"question_id": question.id, "message": "Question posted successfully"}

@app.post("/questions/{question_id}/answers/")
def create_answer(question_id: str, content: str = Form(...), username: str = Form(...)):
    user = session.query(User).filter_by(username=username).first()
    if not user:
        user = User(username=username)
        session.add(user)
        session.commit()
    
    answer = Answer(content=content, user_id=user.id, question_id=question_id)
    session.add(answer)
    session.commit()
    return {"answer_id": answer.id, "message": "Answer posted successfully"}

@app.post("/questions/{question_id}/vote/")
def vote_question(question_id: str, vote_type: VoteType = Query(...)):
    """
    Post a vote to a question.

    This endpoint takes a question ID and a vote type (upvote or downvote) and
    stores the vote in Redis. It then schedules a background job to sync the
    vote to the database.

    :param question_id: The ID of the question to vote on.
    :param vote_type: The type of vote to post (upvote or downvote).
    :return: A message indicating that the vote was registered and will be synced.
    """
    # Check if the question exists
    question = session.query(Question).filter_by(id=question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    
    # Check if vote_type is valid
    if vote_type not in {VoteType.UPVOTE, VoteType.DOWNVOTE}:
        raise HTTPException(status_code=422, detail="Unprocessable Entity: Invalid vote type")
    
    try:
        # Store vote in Redis
        r.incrby(f"question:{question_id}:votes", vote_type.value)
        
        # Schedule vote sync as a background job
        sync_votes_to_db.delay()
        
        return {"message": "Vote registered and will be synced"}
    except redis.RedisError as e:
        raise HTTPException(status_code=500, detail=f"Redis error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")



        
