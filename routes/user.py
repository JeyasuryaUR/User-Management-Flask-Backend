from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from models import User
from database import db
import re

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # Validate payload
    if not data or 'username' not in data or 'email' not in data or 'password' not in data:
        return jsonify({'message': 'Invalid payload'}), 400

    username = data['username']
    email = data['email']
    password = data['password']

    # Validate email
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return jsonify({'message': 'Invalid email'}), 400

    # Validate password length
    if len(password) < 8:
        return jsonify({'message': 'Password must be at least 8 characters long'}), 400

    # Hash password
    hashed_password = generate_password_hash(password)

    # Save user to database
    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

@user_blueprint.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'username': user.username, 'email': user.email} for user in users]), 200