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
    if not data or not isinstance(data, dict) or not data.get('titre') or not data['titre'].strip() or not data.get('contenu') or not data['contenu'].strip():
        return jsonify({'message': "Les champs 'titre' et 'contenu' sont requis et ne doivent pas être vides."}), 400

    try:
        nouveau_postit = PostIt(titre=data['titre'], contenu=data['contenu'])
        db.session.add(nouveau_postit)
        db.session.commit()

        return jsonify({
            'message': 'Post-it créé avec succès',
            'postit_id': nouveau_postit.id
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Erreur lors de la création du post-it', 'error': str(e)}), 500


@api_bp.route('/postits/<int:postit_id>', methods=['PUT'])
def mettre_a_jour_postit(postit_id):
    postit = db.session.get(PostIt, postit_id)
    if not postit:
        return jsonify({'message': 'Post-it non trouvé'}), 404

    data = request.get_json()
    if not data or not isinstance(data, dict):
        return jsonify({'message': "Requête invalide, envoi de données requis."}), 400

    if 'titre' in data and data['titre'].strip():
        postit.titre = data['titre']
    if 'contenu' in data and data['contenu'].strip():
        postit.contenu = data['contenu']

    db.session.commit()
    return jsonify({
        'message': 'Post-it mis à jour avec succès',
        'postit': {'id': postit.id, 'titre': postit.titre, 'contenu': postit.contenu, 'date_creation': postit.date_creation}
    }), 200

@api_bp.route('/postits/<int:postit_id>', methods=['DELETE'])
def supprimer_postit(postit_id):
    """
    Supprime un post-it existant.
    """
    postit = db.session.get(PostIt, postit_id)
    if not postit:
        return jsonify({'message': 'Post-it non trouvé'}), 404

    try:
        db.session.delete(postit)
        db.session.commit()
        return jsonify({'message': 'Post-it supprimé avec succès'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Erreur lors de la suppression du post-it', 'error': str(e)}), 500
