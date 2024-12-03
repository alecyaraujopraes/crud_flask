from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    updated_date = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """Converte o objeto para um dicionário."""
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_date': self.created_date,
            'updated_date': self.updated_date
        }
    
    def __repr__(self):
        return f"<User {self.username}>"