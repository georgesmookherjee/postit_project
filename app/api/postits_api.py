from flask import Blueprint, jsonify, request
from ..models import PostIt
from app import db
from . import api_bp  # On importe api_bp de __init__.py

@api_bp.route('/postits', methods=['GET'])
def obtenir_postits():
    """
    Renvoie tous les post-its au format JSON.
    """
    postits = PostIt.query.order_by(PostIt.id.asc()).all()  # Trie par date de création (du plus ancien au plus récent)
    return jsonify([postit.to_dict() for postit in postits])

@api_bp.route('/postits', methods=['POST'])
def creer_postit():
    """Crée un post-it sans obligation de remplir le titre ou le contenu."""
    data = request.get_json()
    if not data:
        return jsonify({'message': "Requête invalide."}), 400

    titre = data.get('titre', '').strip()
    contenu = data.get('contenu', '').strip()

    nouveau_postit = PostIt(titre=titre, contenu=contenu)
    db.session.add(nouveau_postit)
    db.session.commit()

    return jsonify(nouveau_postit.to_dict()), 201

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

    db.session.delete(postit)
    db.session.commit()
    return jsonify({'message': 'Post-it supprimé avec succès'}), 200

