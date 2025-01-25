from flask import Blueprint, render_template
from app.models import PostIt

# Blueprint pour les pages HTML
html_bp = Blueprint('html', __name__)

@html_bp.route('/', methods=['GET'])
def home():
    return render_template('index.html', nom='Felix le ouf')

@html_bp.route('/postits', methods=['GET'])
def afficher_postits():
    postits = PostIt.query.all()
    postits_data = [
        {'id': p.id, 'titre': p.titre, 'contenu': p.contenu, 'date_creation': p.date_creation}
        for p in postits
    ]
    return render_template('postits.html', postits=postits_data)

