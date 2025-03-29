from flask import jsonify, request
from ..models import PostIt, db
from . import postits_api  # On importe api_bp de __init__.py
from flask_login import login_required, current_user

@postits_api.route('/postits', methods=['GET'])
@login_required
def obtenir_postits():
    """
    Renvoie tous les post-its au format JSON.
    """
    postits = PostIt.query.order_by(PostIt.id.asc()).filter_by(user_id=current_user.id).all()  # Trie par date de création (du plus ancien au plus récent)
    return jsonify([postit.to_dict() for postit in postits])

@postits_api.route('/postits', methods=['POST'])
@login_required
def creer_postit():
    """Crée un post-it sans obligation de remplir le titre ou le contenu."""
    data = request.get_json()
    if not data:
        return jsonify({'message': "Requête invalide."}), 400

    titre = data.get('titre', '').strip()
    contenu = data.get('contenu', '').strip()

    nouveau_postit = PostIt(titre=titre, contenu=contenu, user_id=current_user.id)
    db.session.add(nouveau_postit)
    db.session.commit()

    return jsonify(nouveau_postit.to_dict()), 201

@postits_api.route('/postits/<int:postit_id>', methods=['PUT'])
@login_required
def mettre_a_jour_postit(postit_id):
    postit = db.session.get(PostIt, postit_id)
    if not postit:
        return jsonify({'message': 'Post-it non trouvé'}), 404
    
    # Vérifier si l'utilisateur connecté est le propriétaire
    if postit.user_id != current_user.id:
        return jsonify({'message': 'Non autorisé'}), 403

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

@postits_api.route('/postits/<int:postit_id>', methods=['DELETE'])
@login_required
def supprimer_postit(postit_id):
    """
    Supprime un post-it existant si l'utilisateur en est le propriétaire
    """
    postit = db.session.get(PostIt, postit_id)
    if not postit:
        return jsonify({'message': 'Post-it non trouvé'}), 404
    
    # Vérifier si l'utilisateur connecté est le propriétaire
    if postit.user_id != current_user.id:
        return jsonify({'message': 'Non autorisé'}), 403

    db.session.delete(postit)
    db.session.commit()
    return jsonify({'message': 'Post-it supprimé avec succès'}), 200

