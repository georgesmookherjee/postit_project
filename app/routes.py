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


@routes_app.route('/supprimer/<int:postit_id>', methods=['POST'])
def supprimer_postit(postit_id):
    postit = PostIt.query.get(postit_id)
    if postit:
        db.session.delete(postit)
        db.session.commit()
        flash("Post-it supprimé avec succès", "success")
    else:
        flash("Post-it non trouvé", "error")

    return redirect(url_for('html.afficher_postits'))


@routes_app.route('/', methods=['GET'])
def index():
    return render_template('index.html', nom="Utilisateur")