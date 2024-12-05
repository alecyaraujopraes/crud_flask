from flask import Flask
from app.models import db
from app.routes import users_bp  # Assuming this imports the blueprint


def create_app():
    app = Flask(__name__)
    app.json.sort_keys = False

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    app.register_blueprint(users_bp)
    
    return app

def main():
    app = create_app()
    
    with app.app_context():
        db.create_all()  # Create tables
    
    app.run(debug=True)

if __name__ == '__main__':
    main()