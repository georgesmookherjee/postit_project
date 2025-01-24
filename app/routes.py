from flask import Blueprint, request, jsonify
from .models import PostIt
from . import db

# Initialiser le blueprint
app = Blueprint('app', __name__)

@app.route('/')
def home():
    return "Bienvenue sur votre site de post-it !"

# Route pour tester la connexion à la base de données
@app.route('/ping_db', methods=['GET'])
def ping_db():
    try:
        db.engine.execute('SELECT 1')  # Test de la connexion
        return jsonify({'message': 'Connexion à la base de données réussie'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route pour créer un post-it
@app.route('/créer_postit', methods=['POST'])
def creer_postit():
    data = request.get_json()
    nouveau_postit = PostIt(titre=data['titre'], contenu=data['contenu'])
    db.session.add(nouveau_postit)
    db.session.commit()
    return jsonify({'message': 'Post-it créé avec succès'}), 201

# # Route pour lister tous les post-its
@app.route('/postits', methods=['GET'])
def obtenir_postits():
    postits = PostIt.query.all()
    resultats = [
        {'id': p.id, 'titre': p.titre, 'contenu': p.contenu, 'date_creation': p.date_creation}
        for p in postits
    ]
    return jsonify(resultats), 200


