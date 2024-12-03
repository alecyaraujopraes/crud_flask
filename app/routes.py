from flask import Blueprint, request, jsonify, redirect, url_for
from .models import db, User
from flask import render_template
from datetime import datetime


users_bp = Blueprint('users', __name__)

@users_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return render_template('get_users.html', users=users)


@users_bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return render_template('get_user.html', user=user)


@users_bp.route('/users', methods=['POST'])
def add_user():
    username = request.form['username']
    email = request.form['email']
    new_user = User(username=username, email=email)

    try:
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('users.get_users'))
    except:            
        return "Erro ao adicionar o user"


@users_bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)

    user.username = request.form['username']
    user.email = request.form['email']
    user.updated_date = datetime.utcnow

    try:
        db.session.commit()
        return redirect(f'/users/{id}')
    except:
        return 'There was an issue updating your task'


@users_bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user_to_delete = User.query.get_or_404(id)

    try:
        db.session.delete(user_to_delete)
        db.session.commit()
        return render_template('get_users.html')
    except:
        return 'There was a problem deleting that user'


@users_bp.route('/')
def base():
    return render_template('base.html')