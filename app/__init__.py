from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from dotenv import load_dotenv
from config import current_config
# import blackfire

# Charger les variables d'environnement
load_dotenv()

# Charger les extensions
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()  # Définition globale
login_manager.login_view = "auth_api.login"  # Redirection vers /auth/login si non connecté

@login_manager.unauthorized_handler
def unauthorized():
    return jsonify({"error": "Authentification requise"}), 401

def create_app(testing=False):
    app = Flask(__name__)
    app.config.from_object(current_config)

    # Initialisation des extensions avec l'application
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)  # disponible pour tout le projet

    import os
    os.environ['BLACKFIRE_AGENT_SOCKET'] = 'tcp://blackfire:8307'

    # Wrapping de l'application avec Blackfire (seulement en mode non-test)
    # if not testing:
    #     # utilisation initialize() pour blackfire
    #     blackfire.initialize()

    # Importation des Blueprints
    from .api import postits_api, auth_api, admin_api
    from .views.postits_html import html_bp

    app.register_blueprint(postits_api)
    app.register_blueprint(html_bp)
    app.register_blueprint(auth_api)
    app.register_blueprint(admin_api)

    return app
