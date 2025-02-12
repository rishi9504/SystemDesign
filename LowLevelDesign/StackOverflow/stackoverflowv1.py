from enum import Enum
from threading import Lock
import uuid
from datetime import datetime

# Enum for Vote Type
class VoteType(Enum):
    UPVOTE = 1
    DOWNVOTE = -1

# User Class
class User:
    def __init__(self, username):
        self.user_id = str(uuid.uuid4())
        self.username = username
        self.reputation = 0
        self.lock = Lock()

    def update_reputation(self, points):
        with self.lock:
            self.reputation += points

# Question Class
class Question:
    def __init__(self, title, content, tags, user):
        self.question_id = str(uuid.uuid4())
        self.title = title
        self.content = content
        self.tags = tags
        self.user = user
        self.answers = []
        self.comments = []
        self.votes = 0
        self.lock = Lock()

    def add_answer(self, answer):
        with self.lock:
            self.answers.append(answer)

    def add_comment(self, comment):
        with self.lock:
            self.comments.append(comment)

    def vote(self, vote_type):
        with self.lock:
            self.votes += vote_type.value

# Answer Class
class Answer:
    def __init__(self, content, user):
        self.answer_id = str(uuid.uuid4())
        self.content = content
        self.user = user
        self.comments = []
        self.votes = 0
        self.lock = Lock()

    def add_comment(self, comment):
        with self.lock:
            self.comments.append(comment)

    def vote(self, vote_type):
        with self.lock:
            self.votes += vote_type.value

# Comment Class
class Comment:
    def __init__(self, content, user):
        self.comment_id = str(uuid.uuid4())
        self.content = content
        self.user = user

# StackOverflow System
class StackOverflow:
    def __init__(self):
        self.questions = []
        self.lock = Lock()

    def post_question(self, title, content, tags, user):
        question = Question(title, content, tags, user)
        with self.lock:
            self.questions.append(question)
        return question

    def search_questions(self, keyword=None, tags=None, username=None):
        with self.lock:
            results = []
            for question in self.questions:
                if (keyword and keyword.lower() in question.title.lower()) or \
                   (tags and any(tag in question.tags for tag in tags)) or \
                   (username and question.user.username == username):
                    results.append(question)
            return results

# Simulation
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
    
    # Searching for questions
    results = stack_overflow.search_questions(keyword="singleton")
    for q in results:
        print(f"Found Question: {q.title}")
