from flask import Blueprint

# Création des Blueprints

# Blueprint pour les post-its
postits_api = Blueprint("postits_api", __name__, url_prefix="/api")

# Blueprint pour l'authentification
auth_api = Blueprint("auth_api", __name__, url_prefix="/auth")

# Import des routes associées
from .postits_api import *
from .auth_api import *

