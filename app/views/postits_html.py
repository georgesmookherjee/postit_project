from flask import Blueprint, render_template
from flask_login import login_required, current_user
from ..decorators import admin_required

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

@html_bp.route('/profile-test')
def profile_test():
    try:
        import blackfire
        
        # Créer un contexte de profilage explicite
        profiler = blackfire.profiler.get()
        profiler.start()
        
        try:
            # Code à profiler
            import time
            time.sleep(1)
            
            # Opérations de base de données
            from ..models import PostIt
            count = PostIt.query.count()
            
            result = f"Profiling test successful! Found {count} post-its."
            return result
        finally:
            # Toujours arrêter le profiler, même en cas d'erreur
            profiler.stop()
            
    except Exception as e:
        return f"Erreur de profilage: {str(e)}"   

@html_bp.route('/blackfire-info')
def blackfire_info():
    info = []
    
    try:
        import blackfire
        info.append(f"Version Blackfire: {blackfire.VERSION}")
        
        try:
            # Vérifiez si le profiler est disponible
            profiler = blackfire.profiler.get()
            info.append(f"Profiler disponible: {profiler is not None}")
        except Exception as e:
            info.append(f"Erreur lors de l'accès au profiler: {str(e)}")
        
        # Vérifier les variables d'environnement (masquées pour la sécurité)
        import os
        client_id = os.environ.get('BLACKFIRE_CLIENT_ID', 'Non défini')
        client_token = os.environ.get('BLACKFIRE_CLIENT_TOKEN', 'Non défini')
        info.append(f"BLACKFIRE_CLIENT_ID: {'Défini' if client_id != 'Non défini' else 'Non défini'}")
        info.append(f"BLACKFIRE_CLIENT_TOKEN: {'Défini' if client_token != 'Non défini' else 'Non défini'}")
        
    except Exception as e:
        info.append(f"Erreur générale: {str(e)}")
    
    return "<br>".join(info)

@html_bp.route('/blackfire-help')
def blackfire_help():
    import blackfire
    
    # Récupérer l'aide intégrée si disponible
    help_text = []
    
    # Examiner les fonctions disponibles
    help_text.append("<h2>Fonctions et attributs Blackfire</h2>")
    help_text.append("<pre>")
    for name in dir(blackfire):
        if not name.startswith("_"):  # Ignorer les attributs privés
            attr = getattr(blackfire, name)
            if callable(attr):
                try:
                    help_text.append(f"{name}: {attr.__doc__}")
                except:
                    help_text.append(f"{name}: (fonction sans documentation)")
            else:
                help_text.append(f"{name}: {attr}")
    help_text.append("</pre>")
    
    return "<br>".join(help_text)

@html_bp.route('/profile-direct')
def profile_direct():
    try:
        import blackfire
        
        # Essayer un appel direct à la fonction
        blackfire.profile()(lambda: None)()
        
        # Si nous arrivons ici, cela signifie que le profilage fonctionne
        return "Profilage direct réussi!"
    except Exception as e:
        return f"Erreur de profilage direct: {str(e)}"