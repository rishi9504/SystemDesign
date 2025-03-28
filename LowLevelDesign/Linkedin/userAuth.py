from flask import Flask, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

app = Flask(__name__)
app.secret_key = 'super_secret_key'
JWT_SECRET = 'jwt_secret_key'

# Simulated User Database
USER_DB = {}

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    name = data.get('name')
    password = data.get('password')

    if email in USER_DB:
        return jsonify({"message": "User already exists"}), 400

    hashed_password = generate_password_hash(password)
    USER_DB[email] = {"name": name, "password": hashed_password}
    return jsonify({"message": "User registered successfully"})


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = USER_DB.get(email)
    if not user or not check_password_hash(user['password'], password):
        return jsonify({"message": "Invalid credentials"}), 401

    token = jwt.encode({
        'email': email,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, JWT_SECRET, algorithm='HS256')

    return jsonify({"token": token})


def token_required(func):
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({"message": "Token is missing"}), 401

        try:
            decoded_token = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
            email = decoded_token['email']
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Invalid token"}), 401

        return func(email, *args, **kwargs)

    return wrapper


@app.route('/profile', methods=['GET'])
@token_required
def profile(email):
    user_data = USER_DB.get(email)
    if not user_data:
        return jsonify({"message": "User not found"}), 404

    return jsonify({"name": user_data['name'], "email": email})


if __name__ == '__main__':
    app.run(debug=True)
