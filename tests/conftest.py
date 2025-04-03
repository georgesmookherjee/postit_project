import pytest
from app import create_app, db
import os
import time

# 🔹 Forcer explicitement le mode TESTING avant de créer l'application
os.environ["TESTING_MODE"] = "true"
os.environ["APP_ENV"] = "testing"  # S'assurer que Flask reconnaît bien l'environnement de test

@pytest.fixture(scope="function")
def authenticated_client(client):
    """Fixture qui fournit un client déjà authentifié pour les tests."""
    # Créer un utilisateur de test
    client.post('/auth/register', json={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'testpassword'
    })
    
    # Connecter l'utilisateur
    client.post('/auth/login', json={
        'identifier': 'test@example.com',
        'password': 'testpassword'
    })
    
    return client

@pytest.fixture(scope="function")
def client():
    """Fixture qui initialise l'application Flask en mode test et utilise la base de test."""
    # 🔹 Création de l'application en mode test
    app = create_app(testing=True)

    # 🔹 Vérification stricte de la base de données utilisée
    database_url = os.getenv("TEST_DATABASE_URL")
    app.config["SQLALCHEMY_DATABASE_URI"] = database_url
    app.config["TESTING"] = True

    # 🔹 Vérification supplémentaire pour éviter d'impacter la BDD de dev
    assert "test" in app.config["SQLALCHEMY_DATABASE_URI"], "❌ ERREUR: Mauvaise base utilisée !"

    with app.app_context():
        db.create_all()  # Créer les tables pour le test
        yield app.test_client()  # Exposer le client de test à pytest

        # Nettoyage après les tests
        db.session.remove()  # S'assurer qu'aucune connexion ne reste ouverte
        db.drop_all()  # Supprimer toutes les tables après chaque test
        #time.sleep(1)  # 🔹 Délai pour éviter des problèmes avec PostgreSQL

