from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

app = Flask(__name__)
app.secret_key = 'super_secret_key'
JWT_SECRET = 'jwt_secret_key'

# Simulated Database
USER_DB = {}
CONNECTIONS = {}
MESSAGES = {}
JOB_POSTINGS = []
NOTIFICATIONS = {}

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    name = data.get('name')
    password = data.get('password')

    if email in USER_DB:
        return jsonify({"message": "User already exists"}), 400

    hashed_password = generate_password_hash(password)
    USER_DB[email] = {"name": name, "password": hashed_password, "profile": {}, "connections": [], "messages": []}
    return jsonify({"message": "User registered successfully"})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = USER_DB.get(email)
    if not user or not check_password_hash(user['password'], password):
        return jsonify({"message": "Invalid credentials"}), 401

    token = jwt.encode({'email': email, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, JWT_SECRET, algorithm='HS256')
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

@app.route('/profile', methods=['GET', 'PUT'])
@token_required
def profile(email):
    user_data = USER_DB.get(email)
    if not user_data:
        return jsonify({"message": "User not found"}), 404

    if request.method == 'PUT':
        data = request.get_json()
        user_data['profile'].update(data)
        return jsonify({"message": "Profile updated"})

    return jsonify({"profile": user_data['profile']})

@app.route('/connect/<target_email>', methods=['POST'])
@token_required
def connect(email, target_email):
    if target_email not in USER_DB:
        return jsonify({"message": "User not found"}), 404

    if target_email not in USER_DB[email]['connections']:
        USER_DB[email]['connections'].append(target_email)
        USER_DB[target_email]['connections'].append(email)
        return jsonify({"message": "Connection successful"})

    return jsonify({"message": "Already connected"})

@app.route('/message/<recipient>', methods=['POST'])
@token_required
def message(email, recipient):
    data = request.get_json()
    msg = data.get('message')

    if recipient not in USER_DB:
        return jsonify({"message": "Recipient not found"}), 404

    USER_DB[recipient]['messages'].append({"sender": email, "message": msg})
    return jsonify({"message": "Message sent"})

@app.route('/jobs', methods=['POST', 'GET'])
@token_required
def jobs(email):
    if request.method == 'POST':
        data = request.get_json()
        JOB_POSTINGS.append({"posted_by": email, **data})
        return jsonify({"message": "Job posted"})

    return jsonify({"jobs": JOB_POSTINGS})

@app.route('/search', methods=['GET'])
@token_required
def search(email):
    query = request.args.get('q')
    results = [user for user in USER_DB if query.lower() in user.lower()]
    return jsonify({"results": results})

if __name__ == '__main__':
    app.run(debug=True)
