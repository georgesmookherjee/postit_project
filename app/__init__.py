from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

# Charger les variables d'environnement
load_dotenv()

# Initialisation des extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Configuration de l'application
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')  # URI PostgreSQL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')

    # Initialiser les extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Enregistrer les blueprints
    from .routes import app as routes_app
    app.register_blueprint(routes_app)

    return app
