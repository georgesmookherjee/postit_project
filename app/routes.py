from flask import Blueprint, request, jsonify, render_template, redirect, url_for, send_from_directory
from .models import db, PostIt
from . import db
from flask import flash
import os

# Blueprint pour les routes générales
routes_app = Blueprint('routes', __name__)

@routes_app.route('/postits', methods=['GET'])
def afficher_postits_html():
    postits = PostIt.query.order_by(PostIt.id.asc()).all()
    return render_template("postits.html", postits=postits)

@routes_app.route('/ping_db', methods=['GET'])
def ping_db():
    try:
        db.engine.execute('SELECT 1')
        return jsonify({'message': 'Connexion à la base de données réussie'}), 200
    except Exception as erreur:
        return jsonify({'error': str(erreur)}), 500

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

@routes_app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(routes_app.root_path, 'static'), 'favicon.ico')

