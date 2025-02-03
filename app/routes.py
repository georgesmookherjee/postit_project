from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from .models import db, PostIt
from . import db
from flask import flash

# Blueprint pour les routes générales
routes_app = Blueprint('routes', __name__)

@routes_app.route('/ping_db', methods=['GET'])
def ping_db():
    try:
        db.engine.execute('SELECT 1')
        return jsonify({'message': 'Connexion à la base de données réussie'}), 200
    except Exception as erreur:
        return jsonify({'error': str(erreur)}), 500

@routes_app.route('/modifier/<int:postit_id>', methods=['GET', 'POST'])
def modifier_postit(postit_id):
    postit = PostIt.query.get(postit_id)
    
    if request.method == 'POST':
        postit.titre = request.form['titre']
        postit.contenu = request.form['contenu']
        db.session.commit()
        flash("Post-it modifié avec succès", "success")
        return redirect(url_for('html.afficher_postits'))

    return render_template('modifier_postit.html', postit=postit)


@routes_app.route('/api/postits/<int:postit_id>', methods=['DELETE'])
def supprimer_postit(postit_id):
    postit = db.session.get(PostIt, postit_id)
    if not postit:
        return jsonify({"message": "Post-it non trouvé"}), 404

    try:
        db.session.delete(postit)
        db.session.commit()
        return jsonify({"message": "Post-it supprimé avec succès"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Erreur lors de la suppression", "error": str(e)}), 500



@routes_app.route('/', methods=['GET'])
def index():
    return render_template('index.html', nom="Utilisateur")

