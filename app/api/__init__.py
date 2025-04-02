from flask import Blueprint

# Création des Blueprints

# Blueprint pour les post-its
postits_api = Blueprint("postits_api", __name__, url_prefix="/api")

# Blueprint pour l'authentification
auth_api = Blueprint("auth_api", __name__, url_prefix="/auth")

# Ajoutez le blueprint d'administration
admin_api = Blueprint("admin_api", __name__, url_prefix="/admin/api")

# Import des routes associées
from .postits_api import *
from .auth_api import *
from .admin_api import * 
