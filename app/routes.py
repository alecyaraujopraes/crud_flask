from flask import Blueprint, request, jsonify, redirect
from .models import db, User
from flask import render_template


users_bp = Blueprint('users', __name__)

@users_bp.route('/users', methods=['GET'])
def get_users():
    # Implementar lógica para obter todos os usuários
    return render_template('get_users.html', person=name)

@users_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return render_template('get_users.html', person=name)

@users_bp.route('/users', methods=['POST'])
def add_user():
    task_content = request.form['content']
    new_task = User(content=task_content)

    try:
        db.session.add(new_task)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was an issue adding your task'



@users_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    task = User.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'

    else:
        return render_template('update.html', task=task)
    return render_template('get_users.html', person=name)

@users_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    task_to_delete = User.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'

@users_bp.route('/')
def base():
    return render_template('base.html')