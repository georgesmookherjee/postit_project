from flask import Blueprint, render_template
from ..decorators import admin_required, current_user
from flask_login import login_required

# Blueprint pour les pages HTML
html_bp = Blueprint('html', __name__)

@html_bp.route('/', methods=['GET'])
def home():
    return render_template('index.html', nom='Visiteur')

@html_bp.route('/postits', methods=['GET'])
def afficher_page_postits():
    return render_template('postits.html')  # Ne passe plus les données en contexte

@html_bp.route('/admin', methods=['GET'])
@admin_required
def admin_panel():
    return render_template('admin.html')
