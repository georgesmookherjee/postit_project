from flask import Blueprint, jsonify, request
from app.models import PostIt
from app import db  # Ajoute l'import de db

# Blueprint pour l'API JSON
api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/postits', methods=['GET'])
def obtenir_postits():
    """
    Renvoie tous les post-its au format JSON.
    """
    postits = PostIt.query.all()
    results = [
        {'id': p.id, 'titre': p.titre, 'contenu': p.contenu, 'date_creation': p.date_creation}
        for p in postits
    ]
    return jsonify(results), 200

@api_bp.route('/postits/new', methods=['POST'])
def creer_postit():
    """
    Crée un nouveau post-it.
    """
    data = request.get_json()
    if not data or not isinstance(data, dict) or not data.get('titre') or not data.get('contenu') \
       or not data['titre'].strip() or not data['contenu'].strip():
        return jsonify({'message': "Les champs 'titre' et 'contenu' sont requis et ne doivent pas être vides."}), 400

    try:
        nouveau_postit = PostIt(titre=data['titre'], contenu=data['contenu'])
        db.session.add(nouveau_postit)
        db.session.commit()
        return jsonify({'message': 'Post-it créé avec succès'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Erreur lors de la création du post-it', 'error': str(e)}), 500
