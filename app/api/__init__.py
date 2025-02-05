from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Création de l'instance SQLAlchemy (sans l'attacher à une app tout de suite)
db = SQLAlchemy()

def create_app():
    """Crée et configure l'application Flask"""
    app = Flask(__name__, static_folder='static')

    # Configuration de la base de données
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}" # À adapter selon ton besoin
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Attache SQLAlchemy à l'application
    db.init_app(app)

    # Importation et enregistrement des Blueprints
    from app.routes import routes_app
    from app.views.postits_html import html_bp
    from app.api.postits_api import api_bp
    
    app.register_blueprint(routes_app)
    app.register_blueprint(html_bp)
    app.register_blueprint(api_bp)

    # Création des tables si elles n'existent pas encore
    with app.app_context():
        db.create_all()

    return app

