from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

# Charger les extensions
db = SQLAlchemy()
migrate = Migrate()

# Charger les variables d'environnement
load_dotenv()

def create_app(testing=False):
    app = Flask(__name__)

    if testing:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('TEST_DATABASE_URL')
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')

    db.init_app(app)
    migrate.init_app(app, db)

    # Enregistrer les Blueprints
    from .routes import routes_app
    from .api.postits_api import api_bp
    from .views.postits_html import html_bp

    app.register_blueprint(routes_app)
    app.register_blueprint(api_bp)
    app.register_blueprint(html_bp)

    return app


