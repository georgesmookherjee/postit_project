from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from dotenv import load_dotenv
from config import current_config
import os
# from blackfire import probe
# import blackfire

# blackfire.patch_all()

# # Initialisation de l'agent Blackfire
# probe.initialize()

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

    # Importation des Blueprints
    from .api import postits_api, auth_api, admin_api
    from .views.postits_html import html_bp

    app.register_blueprint(postits_api)
    app.register_blueprint(html_bp)
    app.register_blueprint(auth_api)
    app.register_blueprint(admin_api)

    if app.config.get('ENABLE_BLACKFIRE') and 'BLACKFIRE_SERVER_ID' in os.environ:
        try:
            import blackfire
            from blackfire import BlackfireMiddleware
            app.wsgi_app = BlackfireMiddleware(app.wsgi_app)
        except ImportError:
            pass
    # # Dans votre app Flask
    # @app.route('/')
    # @probe.profile()
    # def bonjour():
    #     return 'Hello World'

    return app
