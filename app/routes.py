from flask import Blueprint, request, jsonify, render_template
from .models import PostIt
from . import db

# Initialiser le blueprint
app = Blueprint('app', __name__)

@app.route('/')
def home():
    return render_template('index.html')

# Route pour tester la connexion à la base de données
@app.route('/ping_db', methods=['GET'])
def ping_db():
    try:
        db.engine.execute('SELECT 1')  # Test de la connexion
        return jsonify({'message': 'Connexion à la base de données réussie'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/créer_postit', methods=['POST'])
def creer_postit():
    data = request.get_json()
    if not data or not data.get('titre') or not data.get('contenu'):
        return jsonify({'message': "Les champs 'titre' et 'contenu' sont requis."}), 400
    nouveau_postit = PostIt(titre=data['titre'], contenu=data['contenu'])
    db.session.add(nouveau_postit)
    db.session.commit()
    return jsonify({'message': 'Post-it créé avec succès'}), 201

@app.route('/postits', methods=['GET'])
def obtenir_postits():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    postits = PostIt.query.paginate(page=page, per_page=per_page, error_out=False)
    results = [
        {'id': p.id, 'titre': p.titre, 'contenu': p.contenu, 'date_creation': p.date_creation}
        for p in postits.items
    ]
    return jsonify(results), 200

