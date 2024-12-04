import pytest
import sys
from flask import Flask

sys.path.append("./")
from app.models import db
from app.models import User


@pytest.fixture
def client():
    """
    Configura o cliente de teste com um banco de dados SQLite em memória.
    """
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Cria as tabelas no banco de dados em memória
        yield client
        with app.app_context():
            db.session.remove()
            db.drop_all()  # Limpa o banco após o teste

def test_get_users_success(client):
    """
    Testa o endpoint /users com dados no banco.
    """
    # Arrange: Cria usuários no banco
    user1 = User(username="Alice", email="alice@example.com")
    user2 = User(username="Bob", email="bob@example.com")
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

    # Act: Faz a requisição GET
    response = client.get('http://localhost:5000/users')

    # Assert: Verifica os resultados
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 2
    assert data[0]['username'] == "Alice"
    assert data[1]['username'] == "Bob"

def test_get_users_empty(client):
    """
    Testa o endpoint /users quando o banco está vazio.
    """
    response = client.get('http://localhost:5000/users')
    assert response.status_code == 200
    data = response.get_json()
    assert data == []  # Sem usuários no banco

def test_get_users_error(client, monkeypatch):
    """
    Testa o comportamento do endpoint /users quando ocorre um erro.
    """
    # Simula erro na consulta ao banco
    def mock_query_all():
        raise Exception("Simulated database error")
    monkeypatch.setattr('app.models.User.query', lambda: mock_query_all())

    response = client.get('http://localhost:5000/users')
    assert response.status_code == 400
    data = response.get_json()
    assert data['message'] == "Error to retrieve users"