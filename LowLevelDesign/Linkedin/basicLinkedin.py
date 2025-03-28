import jwt
import datetime
from typing import Tuple
import os
import hashlib
import hmac

def generate_password_hash(password: str) -> Tuple[bytes, bytes]:
    """
    Hash the provided password with a randomly-generated salt and return the
    salt and hash to store in the database.
    """
    salt = os.urandom(16)
    pw_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return salt, pw_hash

def check_password_hash(salt: bytes, pw_hash: bytes, password: str) -> bool:
    """
    Given a previously-stored salt and hash, and a password provided by a user
    trying to log in, check whether the password is correct.
    """
    return hmac.compare_digest(
        pw_hash,
        hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    )
    

class User:
    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.password = generate_password_hash(password)
        self.profile = {}
        self.connections = []
        self.messages = []

class UserAuthenticationSystem:
    JWT_SECRET = 'jwt_secret_key'
    USER_DB = {}
    JOB_POSTINGS = []

    @classmethod
    def register(cls, email, name, password):
        if email in cls.USER_DB:
            return "User already exists"
        cls.USER_DB[email] = User(email, name, password)
        return "User registered successfully"

    @classmethod
    def login(cls, email, password):
        user = cls.USER_DB.get(email)
        if not user or not check_password_hash(user.password, password):
            return "Invalid credentials"
        token = jwt.encode({'email': email, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, 
                           cls.JWT_SECRET, algorithm='HS256')
        return token

    @classmethod
    def update_profile(cls, email, profile_data):
        user = cls.USER_DB.get(email)
        if not user:
            return "User not found"
        user.profile.update(profile_data)
        return "Profile updated"

    @classmethod
    def connect(cls, email, target_email):
        if target_email not in cls.USER_DB:
            return "User not found"
        user = cls.USER_DB[email]
        target_user = cls.USER_DB[target_email]
        if target_email not in user.connections:
            user.connections.append(target_email)
            target_user.connections.append(email)
            return "Connection successful"
        return "Already connected"

    @classmethod
    def send_message(cls, email, recipient_email, message):
        if recipient_email not in cls.USER_DB:
            return "Recipient not found"
        recipient = cls.USER_DB[recipient_email]
        recipient.messages.append({"sender": email, "message": message})
        return "Message sent"

    @classmethod
    def post_job(cls, email, job_data):
        cls.JOB_POSTINGS.append({"posted_by": email, **job_data})
        return "Job posted"

    @classmethod
    def search_users(cls, query):
        return [email for email in cls.USER_DB if query.lower() in email.lower()]
