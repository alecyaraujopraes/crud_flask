from flask import Blueprint, request, jsonify, redirect, url_for
from .models import db, User
from flask import render_template
from datetime import datetime
from email_validator import validate_email, EmailNotValidError


users_bp = Blueprint('users', __name__)

@users_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()

    user_list = [user.to_dict() for user in users]
    try:
        return jsonify(user_list), 200
    except:
        return jsonify({"message": "Error to retrieve users"}), 400


@users_bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    user_list = [user.to_dict()]
    try:
        return jsonify(user_list), 200
    except:
        return jsonify({"message": "Error to retrieve details of user"}), 400


@users_bp.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()

    username = data.get('username')
    email = data.get('email')

    if not username or not email:
        return jsonify({"error": "Username and e-mail are required"}), 400

    if User.query.filter(User.email.ilike(email)).first():
        return jsonify({"error": "Email is already in use."}), 400

    try:
        validate_email(email)
    except EmailNotValidError as e:
        return jsonify({"error": "E-mail not valid"}), 400
    
    new_user = User(username=username, email=email)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User added"}), 200
    except:            
        return jsonify({"message": "Failed to add user"}), 400


@users_bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)

    if not user:
        return jsonify({"error": "Usuário não encontrado"}), 404
    
    data = request.get_json()

    username = data.get('username')
    email = data.get('email')

    if not username or not email:
        return jsonify({"error": "Username and e-mail are required"}), 400

    user.username = username
    user.email = email
    user.updated_date = datetime.utcnow()

    try:
        db.session.commit()
        return jsonify({"message": "User updated"}), 200
    except:
        return jsonify({"message": "Failed to update user"}), 400


@users_bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user_to_delete = User.query.get_or_404(id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    try:
        db.session.delete(user_to_delete)
        db.session.commit()
        return jsonify({"message": "User deleted successfully"}), 200
    except:
        return jsonify({"message": "Failed to delete user"}), 400


@users_bp.route('/')
def base():
    return render_template('base.html')