from enum import Enum
from threading import Lock
import uuid
from datetime import datetime
import redis
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from fastapi import FastAPI, HTTPException
from celery import Celery

# Initialize Redis and Database Session
r = redis.Redis(host='localhost', port=6379, db=0)
Session = sessionmaker(bind=db_engine)
session = Session()

# Initialize FastAPI for creating RESTful API endpoints
app = FastAPI()

# Initialize Celery for background job processing
celery_app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

# Enum for Vote Type (Upvote or Downvote)
class VoteType(Enum):
    UPVOTE = 1
    DOWNVOTE = -1

# User Class to manage user information and reputation
class User:
    def __init__(self, username):
        self.user_id = str(uuid.uuid4())  # Generate unique user ID
        self.username = username
        self.reputation = 0  # Initial reputation score

    def update_reputation(self, points):
        """Updates user reputation using Redis atomic increment."""
        r.incrby(f"user:{self.user_id}:reputation", points)

# Question Class to manage questions, answers, comments, and votes
class Question:
    def __init__(self, title, content, tags, user):
        self.question_id = str(uuid.uuid4())  # Generate unique question ID
        self.title = title
        self.content = content
        self.tags = tags  # List of associated tags
        self.user = user  # User who posted the question
        self.answers = []  # List of answers
        self.comments = []  # List of comments

    def add_answer(self, answer):
        """Adds an answer to the question."""
        self.answers.append(answer)

    def add_comment(self, comment):
        """Adds a comment to the question."""
        self.comments.append(comment)

    def vote(self, vote_type):
        """Handles voting for the question using Redis."""
        r.incrby(f"question:{self.question_id}:votes", vote_type.value)

# Answer Class to manage answers and their votes
class Answer:
    def __init__(self, content, user):
        self.answer_id = str(uuid.uuid4())  # Generate unique answer ID
        self.content = content
        self.user = user  # User who posted the answer
        self.comments = []  # List of comments on the answer

    def add_comment(self, comment):
        """Adds a comment to the answer."""
        self.comments.append(comment)

    def vote(self, vote_type):
        """Handles voting for the answer using Redis."""
        r.incrby(f"answer:{self.answer_id}:votes", vote_type.value)

# Comment Class to manage comments on questions and answers
class Comment:
    def __init__(self, content, user):
        self.comment_id = str(uuid.uuid4())  # Generate unique comment ID
        self.content = content
        self.user = user  # User who posted the comment

# StackOverflow System Class to manage overall functionality
class StackOverflow:
    def __init__(self):
        self.questions = []  # List of all posted questions

    def post_question(self, title, content, tags, user):
        """Creates and stores a new question."""
        question = Question(title, content, tags, user)
        self.questions.append(question)
        return question

    def search_questions(self, keyword=None, tags=None, username=None):
        """Search for questions based on keyword, tags, or username."""
        results = []
        for question in self.questions:
            if (keyword and keyword.lower() in question.title.lower()) or \
               (tags and any(tag in question.tags for tag in tags)) or \
               (username and question.user.username == username):
                results.append(question)
        return results

    def persist_votes_to_db(self):
        """Periodically persist vote counts from Redis to the database."""
        for question in self.questions:
            votes = int(r.get(f"question:{question.question_id}:votes") or 0)
            session.execute("UPDATE questions SET votes = :votes WHERE question_id = :id", 
                            {"votes": votes, "id": question.question_id})
        session.commit()

# Celery Task for Background Vote Syncing
@celery_app.task
def sync_votes_to_db():
    """Background task to periodically sync vote counts from Redis to the database."""
    stack_overflow = StackOverflow()
    stack_overflow.persist_votes_to_db()

# FastAPI Endpoints for API integration
@app.post("/questions/")
def create_question(title: str, content: str, tags: list, username: str):
    """API endpoint to create a new question."""
    user = User(username)
    question = stack_overflow.post_question(title, content, tags, user)
    return {"question_id": question.question_id, "message": "Question posted successfully"}

@app.get("/questions/search/")
def search_questions(keyword: str = None, tags: list = None, username: str = None):
    """API endpoint to search for questions."""
    results = stack_overflow.search_questions(keyword, tags, username)
    return [{"question_id": q.question_id, "title": q.title} for q in results]

@app.post("/questions/{question_id}/vote/")
def vote_question(question_id: str, vote_type: VoteType):
    """API endpoint to vote on a question."""
    r.incrby(f"question:{question_id}:votes", vote_type.value)
    sync_votes_to_db.delay()  # Schedule vote sync as a background job
    return {"message": "Vote registered and will be synced"}

# Simulation for testing functionalities
if __name__ == "__main__":
    stack_overflow = StackOverflow()
    user1 = User("Alice")
    user2 = User("Bob")

    # User posts a question
    question = stack_overflow.post_question("How to implement a singleton in Python?", "I need help with singletons.", ["Python", "Design Patterns"], user1)
    
    # User answers the question
    answer = Answer("You can use a metaclass or decorators.", user2)
    question.add_answer(answer)
    
    # User votes on the answer
    answer.vote(VoteType.UPVOTE)
    user2.update_reputation(10)
    
    # Persist votes to database periodically using Celery
    sync_votes_to_db.delay()
    
    # Searching for questions
    results = stack_overflow.search_questions(keyword="singleton")
    for q in results:
        print(f"Found Question: {q.title}")
