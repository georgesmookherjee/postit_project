from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from config import current_config
#import os

# Charger les extensions
db = SQLAlchemy()
migrate = Migrate()

# Charger les variables d'environnement
load_dotenv()

def create_app(testing=False):
    app = Flask(__name__)
    app.config.from_object(current_config)  # Charge la config définie dans config.py automatiquement
        
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


