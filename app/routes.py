from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from .models import db, PostIt
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


@toutes_app.route('/ajouter', methods=['GET', 'POST'])
def ajouter_postit():
    if request.method == 'POST':
        titre = request.form['titre']
        contenu = request.form['contenu']
        nouveau_postit = PostIt(titre=titre, contenu=contenu)
        db.session.add(nouveau_postit)
        db.session.commit()
        return redirect(url_for('html.afficher_postits'))  # Redirige vers la liste
    return render_template('ajouter_postit.html')

@toutes_app.route('/')
def index():
    return render_template('index.html', nom="Utilisateur")