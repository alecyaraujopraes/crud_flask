# Flask CRUD Application

## Overview
This repository contains a Flask-based web application that implements CRUD (Create, Read, Update, Delete) operations for managing `User` entities. The application is structured for scalability and includes unit tests implemented with `pytest` to ensure reliability.

## Features
- **CRUD Operations**: Manage user entities via RESTful API endpoints.
- **Validation**: Email validation using the `email-validator` package.
- **Database**: Integration with SQLAlchemy for database ORM.
- **Error Handling**: Robust error handling for edge cases.
- **Unit Testing**: Comprehensive test suite using `pytest` and `unittest.mock`.

## Technologies Used
- **Framework**: Flask
- **Database**: SQLAlchemy
- **Testing**: Pytest, Unittest Mock
- **Validation**: email-validator

## Prerequisites
Ensure you have the following installed:
- Python 3.8+
- pip (Python package manager)
- A database server compatible with SQLAlchemy (e.g., SQLite, PostgreSQL, MySQL)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/flask-crud-app.git
   cd flask-crud-app
   ```

2. **Create a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate   # For Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**:
   Update the `SQLALCHEMY_DATABASE_URI` in the configuration file (e.g., `config.py`) to point to your preferred database.

   Initialize the database:
   ```bash
   flask db upgrade
   ```

5. **Run the Application**:
   ```bash
   flask run
   ```

   The application will be available at `http://127.0.0.1:5000/`.

## API Endpoints

### Users Resource

#### GET `/users`
Retrieve a list of all users.
- **Response**:
  ```json
  [
      {
          "id": 1,
          "username": "user1",
          "email": "user1@example.com",
          "created_date": "Tue, 03 Dec 2024 10:47:51 GMT",
          "updated_date": "Tue, 03 Dec 2024 10:47:51 GMT"
      }
  ]
  ```

#### GET `/users/<int:id>`
Retrieve details of a specific user.
- **Response**:
  ```json
  {
      "id": 1,
      "username": "testuser",
      "email": "test@example.com",
      "created_date": "Tue, 03 Dec 2024 10:53:51 GMT",
      "updated_date": "Tue, 03 Dec 2024 10:53:51 GMT"
  }
  ```

#### POST `/users`
Create a new user.
- **Request Body**:
  ```json
  {
      "username": "newuser",
      "email": "new@example.com"
  }
  ```
- **Response**:
  ```json
  {
      "id": 2,
      "username": "newuser",
      "email": "new@example.com",
      "created_date": "...",
      "updated_date": "..."
  }
  ```

#### PUT `/users/<int:id>`
Update an existing user.
- **Request Body**:
  ```json
  {
      "username": "updateduser",
      "email": "updated@example.com"
  }
  ```
- **Response**:
  ```json
  {
      "message": "User updated"
  }
  ```

#### DELETE `/users/<int:id>`
Delete a user.
- **Response**:
  ```json
  {
      "message": "User deleted successfully"
  }
  ```

## Running Unit Tests

1. **Run All Tests**:
   ```bash
   pytest
   ```

2. **Test Coverage Report** (Optional):
   Install `pytest-cov`:
   ```bash
   pip install pytest-cov
   ```
   Run with coverage:
   ```bash
   pytest --cov=app
   ```

## Project Structure
```
flask-crud-app/
├── app/
│   ├── __init__.py
│   ├── models.py       # Database models
│   ├── routes.py       # API endpoints
│   └── config.py       # Configuration settings
├── tests/
│   ├── __init__.py
│   └── test_users.py   # Unit tests for User endpoints
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── run.py              # Application entry point
```

## Contributing

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push to the branch.
5. Open a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

For any questions or issues, feel free to open an issue in the repository or contact the maintainer.
