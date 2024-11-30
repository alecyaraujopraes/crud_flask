from flask import Blueprint, request, jsonify
from .models import db, User
from flask import render_template


users_bp = Blueprint('users', __name__)

@users_bp.route('/users', methods=['GET'])
def get_users():
    # Implementar lógica para obter todos os usuários
    return render_template('begin.html', person=name)

@users_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # Implementar lógica para obter um usuário específico
    pass

@users_bp.route('/users', methods=['POST'])
def add_user():
    # Implementar lógica para adicionar um novo usuário
    pass

@users_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    # Implementar lógica para atualizar um usuário existente
    pass

@users_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    # Implementar lógica para deletar um usuário
    pass