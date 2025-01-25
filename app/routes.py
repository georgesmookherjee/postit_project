from flask import Blueprint, request, jsonify, render_template
from .models import PostIt
from . import db

# Blueprint pour les routes générales
toutes_app = Blueprint('routes', __name__)

@toutes_app.route('/ping_db', methods=['GET'])
def ping_db():
    try:
        db.engine.execute('SELECT 1')  # Test de la connexion
        return jsonify({'message': 'Connexion à la base de données réussie'}), 200
    except Exception as erreur:
        return jsonify({'error': str(erreur)}), 500



