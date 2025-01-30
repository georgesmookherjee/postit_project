from app.models import PostIt, db
from run import app

def test_create_postit(client):
    """
    Teste la création d'un post-it dans la base de données.
    """
    with client.application.app_context():  # Utilise le client Flask pour obtenir le contexte
        postit = PostIt(titre="Test Modèle", contenu="Contenu du modèle")
        db.session.add(postit)
        db.session.commit()

        # Vérifie que le post-it a été créé
        assert postit.id is not None
