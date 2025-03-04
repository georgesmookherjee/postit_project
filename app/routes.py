from flask import Blueprint, request, jsonify, render_template, redirect, url_for, send_from_directory, flash
from .models import PostIt
from app import db
import os

# Blueprint pour les routes générales
routes_app = Blueprint('routes', __name__)

@routes_app.route('/postits', methods=['GET'])
def afficher_postits_html():
    postits = PostIt.query.order_by(PostIt.id.asc()).all()
    return render_template("postits.html", postits=postits)


@routes_app.route('/', methods=['GET'])
def index():
    return render_template('index.html', nom="Utilisateur")

# @routes_app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(routes_app.root_path, 'static'), 'favicon.ico')

# @routes_app.route('/ping_db', methods=['GET'])
# def ping_db():
#     try:
#         db.engine.execute('SELECT 1')
#         return jsonify({'message': 'Connexion à la base de données réussie'}), 200
#     except Exception as erreur:
#         return jsonify({'error': str(erreur)}), 500

