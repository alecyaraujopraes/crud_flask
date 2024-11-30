from flask import Flask
from app.models import db
from app.routes import users_bp
from flask import render_template

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # Use o SQLite como banco de dados
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()
    app.register_blueprint(users_bp)

# @app.route('/')
# def get_users():
#     # Implementar lógica para obter todos os usuários
#     return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True)