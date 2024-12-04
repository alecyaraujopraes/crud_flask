from flask import Flask
from app.models import db
from app.routes import users_bp  # Assuming this imports the blueprint

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize database
    db.init_app(app)
    
    # Register blueprints
    app.register_blueprint(users_bp)
    
    return app

def main():
    app = create_app()
    
    with app.app_context():
        db.create_all()  # Create tables
    
    app.run(debug=True)

if __name__ == '__main__':
    main()
