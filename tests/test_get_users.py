import pytest
from unittest.mock import patch, MagicMock
from app.models import User


@pytest.fixture
def mock_user():
    """Return a mock user instance."""
    return User(id=1, username="testuser", email="test@example.com")


@patch("app.routes.User.query")
def test_get_users(mock_query, client):
    mock_query.all.return_value = [
        User(id=1, username="user1", email="user1@example.com"),
        User(id=2, username="user2", email="user2@example.com"),
    ]
    response = client.get("/users")
    assert response.status_code == 200
    assert response.json == [
        {"id": 1, "username": "user1", "email": "user1@example.com"},
        {"id": 2, "username": "user2", "email": "user2@example.com"},
    ]


@patch("app.routes.User.query")
def test_get_user(mock_query, client, mock_user):
    mock_query.get_or_404.return_value = mock_user
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json == {
        "id": 1,
        "username": "testuser",
        "email": "test@example.com",
    }


@patch("app.routes.db.session")
@patch("app.routes.User.query")
def test_add_user(mock_query, mock_session, client):
    mock_query.filter.return_value.first.return_value = None
    response = client.post(
        "/users",
        json={"username": "newuser", "email": "new@example.com"},
    )
    assert response.status_code == 200
    assert response.json == {"message": "User added"}


@patch("app.routes.db.session")
@patch("app.routes.User.query")
def test_update_user(mock_query, mock_session, client, mock_user):
    mock_query.get_or_404.return_value = mock_user
    response = client.put(
        "/users/1",
        json={"username": "updateduser", "email": "updated@example.com"},
    )
    assert response.status_code == 200
    assert response.json == {"message": "User updated"}


@patch("app.routes.db.session")
@patch("app.routes.User.query")
def test_delete_user(mock_query, mock_session, client, mock_user):
    mock_query.get_or_404.return_value = mock_user
    response = client.delete("/users/1")
    assert response.status_code == 200
    assert response.json == {"message": "User deleted successfully"}
