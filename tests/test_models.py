from app.models import PostIt, db

def test_create_postit():
    """
    Teste la création d'un post-it dans la base de données.
    """
    postit = PostIt(titre="Test Modèle", contenu="Contenu du modèle")
    db.session.add(postit)
    db.session.commit()

    assert postit.id is not None
    assert postit.titre == "Test Modèle"
    assert postit.contenu == "Contenu du modèle"
