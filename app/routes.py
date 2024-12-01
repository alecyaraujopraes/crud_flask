from flask import Blueprint, request, jsonify, redirect
from .models import db, User
from flask import render_template
from datetime import datetime


users_bp = Blueprint('users', __name__)

@users_bp.route('/get/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return render_template('get_users.html', users=users)


@users_bp.route('/get/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return render_template('get_user.html', user=user)


@users_bp.route('/post/users', methods=['POST'])
def add_user():
    username = request.form['username']
    email = request.form['email']
    new_user = User(username=username, email=email)

    try:
        db.session.add(new_user)
        db.session.commit()
        return redirect('/get/users')
    except:            
        return redirect('/get/users')


@users_bp.route('/put/users/<int:id>', methods=['PUT', 'GET'])
def update_user(id):
    user = User.query.get_or_404(id)

    user.username = request.form['username']
    user.email = request.form['email']
    user.updated_date = datetime.utcnow

    try:
        db.session.commit()
        return redirect('/get/users')
    except:
        return 'There was an issue updating your user'

    return render_template('get_users.html')


@users_bp.route('/delete/users/<int:id>', methods=['DELETE','GET'])
def delete_user(id):
    user_to_delete = User.query.get_or_404(id)

    try:
        db.session.delete(user_to_delete)
        db.session.commit()
        return redirect('/get/users')
    except:
        return 'There was a problem deleting that user'


@users_bp.route('/')
def base():
    return render_template('base.html')