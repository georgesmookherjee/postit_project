<<<<<<< HEAD
import os
import pytest
from app import create_app, db
from app.models import PostIt

@pytest.fixture
def client():
    app = create_app(testing=True)
    app.config['TESTING'] = True

    with app.app_context():
        db.create_all()  # Crée les tables pour les tests
    with app.test_client() as client:
        yield client
    with app.app_context():
        db.drop_all()  # Supprime les tables après les tests

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200

def test_creer_postit(client):
    response = client.post('/api/postits/new', json={"titre": "Test Post-It", "contenu": "Ceci est un test"})
    assert response.status_code == 201
    assert response.json['message'] == "Post-it créé avec succès"

def test_postit_saved_in_database(client):
    response = client.post('/api/postits/new', json={"titre": "Test DB", "contenu": "Contenu de test"})
    assert response.status_code == 201
    with client.application.app_context():
        postit = PostIt.query.filter_by(titre="Test DB").first()
        assert postit is not None
        assert postit.contenu == "Contenu de test"

def test_creer_postit_champs_requis(client):
    response = client.post('/api/postits/new', json={})
    assert response.status_code == 400
    assert response.json['message'] == "Les champs 'titre' et 'contenu' sont requis et ne doivent pas être vides."

def test_obtenir_postits_pagination(client):
    response = client.get('/api/postits?page=1&per_page=5')
    assert response.status_code == 200
    assert len(response.json) <= 5
=======
# import os
# import pytest
# from app import create_app, db


# @pytest.fixture
# def client():
#     # Créer une application Flask en mode test
#     app = create_app(testing=True)  # Activer la configuration pour les tests
#     app.config['TESTING'] = True
#     print("Base de données utilisée pour les tests :", app.config['SQLALCHEMY_DATABASE_URI'])

#     # Initialiser la base de données pour les tests
#     with app.app_context():
#         db.create_all()  # Crée les tables dans la base de données de test
    
#     with app.test_client() as client:
#         yield client  # Fournir le client pour les tests
    
#     # Nettoyer la base après les tests
#     # with app.app_context():
#     #     db.session.remove()
#     #     db.drop_all()

# def test_homepage(client):
#     # Tester la route d'accueil
#     response = client.get('/')
#     assert response.status_code == 200

# def test_créer_postit(client):
#     # Simuler une requête POST vers la route /add_postit
#     response = client.post('/créer_postit', json={"titre": "Test Post-It", "contenu": "Ceci est un test"})
    
#     # Vérifie que la réponse HTTP est 200 (OK)
#     assert response.status_code == 201
    
#     # Vérifie que la réponse contient un message de succès
#     assert response.json['message'] == "Post-it créé avec succès" # Ajuste ce message si nécessaire

# def test_postit_saved_in_database(client):
#     """
#     Teste si la route /créer_postit permet de créer un Post-It
#     et retourne le bon code de statut et message.
#     """
        
#     # Simuler une requête POST pour créer un Post-It
#     client.post('/créer_postit', json={"titre": "Test DB", "contenu": "Contenu de test"})

#     # Vérifier que les données sont bien enregistrées
#     from app.models import PostIt  # Importe le modèle PostIt
#     with client.application.app_context():
#         postit = PostIt.query.filter_by(titre="Test DB").first()
#         assert postit is not None  # Vérifie que le Post-It existe
#         assert postit.contenu == "Contenu de test"  # Vérifie le contenu du Post-It

# def test_creer_postit_champs_requis(client):
#     response = client.post('/créer_postit', json={})
#     assert response.status_code == 400
#     assert "Les champs 'titre' et 'contenu' sont requis." in response.json['message']

# def test_creer_postit_champs_requis(client):
#     response = client.post('/créer_postit', json={})
#     assert response.status_code == 400
#     assert response.json['message'] == "Les champs 'titre' et 'contenu' sont requis."

# def test_obtenir_postits_pagination(client):
#     response = client.get('/postits?page=1&per_page=5')
#     assert response.status_code == 200
#     assert len(response.json) <= 5



>>>>>>> organisation_des_tests_V2
