# fichier de cécorateur de routes pour les admins
from functools import wraps
from flask import abort, flash, redirect, url_for
from flask_login import current_user

from functools import wraps
from flask import abort, flash, redirect, url_for, render_template
from flask_login import current_user, login_required

def is_admin():
    return current_user.is_authenticated and current_user.is_administrator()

def admin_required(f):
    @wraps(f)
    @login_required
    def decorated_function(*args, **kwargs):
        if not is_admin():
            return render_template('error.html', message="Accès non autorisé. Vous devez être administrateur."), 403
        return f(*args, **kwargs)
    return decorated_function