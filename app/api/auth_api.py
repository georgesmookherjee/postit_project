from flask import request, jsonify, session
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash
from ..models import db, User
from .. import login_manager
from . import auth_api

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Route d'inscription
@auth_api.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    print("Données reçues pour l'inscription :", data)  # Ajout d'un log

    if not data or not data.get('username') or not data.get('email') or not data.get('password'):
        print("Erreur: Champs obligatoires manquants")
        return jsonify({"error": "Champs obligatoires manquants"}), 400

    if User.query.filter_by(email=data['email']).first():
        print("Erreur: Email déjà utilisé")
        return jsonify({"error": "Email déjà utilisé"}), 400

    if User.query.filter_by(username=data['username']).first():
        print("Erreur: Nom d'utilisateur déjà utilisé")
        return jsonify({"error": "Nom d'utilisateur déjà utilisé"}), 400

    new_user = User(username=data['username'], email=data['email'])
    new_user.set_password(data['password'])  # Vérifie bien que cette méthode existe dans ton modèle User
    db.session.add(new_user)
    
    try:
        db.session.commit()
        print("Utilisateur ajouté avec succès")
        return jsonify({"message": "Inscription réussie"}), 201
    except Exception as e:
        print("Erreur lors de l'ajout à la base de données :", str(e))
        db.session.rollback()
        return jsonify({"error": "Erreur interne"}), 500
    
# Route de connexion
@auth_api.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
    if not data or not data.get('identifier') or not data.get('password'):
        return jsonify({"error": "Champs obligatoires manquants"}), 400

    # Recherche l'utilisateur avec l'email OU le username
    user = User.query.filter((User.email == data['identifier']) | (User.username == data['identifier'])).first()

    if not user or not user.check_password(data['password']):
        return jsonify({"error": "Identifiants incorrects"}), 401

    login_user(user)
    return jsonify({"message": "Connexion réussie"}), 200

# Route de déconnexion
@auth_api.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Déconnexion réussie"}), 200

@auth_api.route('/status', methods=['GET'])
def status():
    if current_user.is_authenticated:
        return jsonify({"logged_in": True, "username": current_user.username}), 200
    return jsonify({"logged_in": False}), 401
