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
