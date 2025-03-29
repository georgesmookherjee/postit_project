from flask import Blueprint, render_template

# Blueprint pour les pages HTML
html_bp = Blueprint('html', __name__)

@html_bp.route('/', methods=['GET'])
def home():
    return render_template('index.html', nom='Visiteur')

@html_bp.route('/postits', methods=['GET'])
def afficher_page_postits():
    return render_template('postits.html')  # Ne passe plus les données en contexte
