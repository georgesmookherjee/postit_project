from flask import jsonify, request
from flask_login import login_required, current_user
from ..models import User, PostIt, db
from .. import login_manager
from . import admin_api  # Importez le blueprint depuis __init__.py

# Vérifiez si l'utilisateur est admin
def is_admin():
    return current_user.is_authenticated and getattr(current_user, 'is_admin', False)

# Décorateur pour restreindre l'accès aux admins
def admin_required(f):
    @login_required
    def decorated_function(*args, **kwargs):
        if not is_admin():
            return jsonify({"error": "Accès non autorisé"}), 403
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    return decorated_function

@admin_api.route('/users', methods=['GET'])
@admin_required
def get_all_users():
    users = User.query.all()
    return jsonify([{
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'is_admin': getattr(user, 'is_admin', False),
        'postits_count': len(user.postits)
    } for user in users])

@admin_api.route('/users/<int:user_id>/make-admin', methods=['PUT'])
@admin_required
def make_admin(user_id):
    user = User.query.get_or_404(user_id)
    user.is_admin = True
    db.session.commit()
    return jsonify({'message': f"L'utilisateur {user.username} est maintenant administrateur"})

@admin_api.route('/users/<int:user_id>/revoke-admin', methods=['PUT'])
@admin_required
def revoke_admin(user_id):
    user = User.query.get_or_404(user_id)
    if user.id == current_user.id:
        return jsonify({'error': "Vous ne pouvez pas révoquer vos propres droits d'administrateur"}), 400
    user.is_admin = False
    db.session.commit()
    return jsonify({'message': f"Les droits d'administrateur de {user.username} ont été révoqués"})

@admin_api.route('/stats', methods=['GET'])
@admin_required
def get_stats():
    users_count = User.query.count()
    postits_count = PostIt.query.count()
    
    return jsonify({
        'users_total': users_count,
        'postits_total': postits_count,
        'avg_postits_per_user': round(postits_count / users_count, 2) if users_count > 0 else 0
    })