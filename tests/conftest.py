import pytest
from app import create_app, db

@pytest.fixture
def client():
    """
    Initialise l'application Flask en mode test et fournit un client de test.
    """
    app = create_app(testing=True)
    app.config['TESTING'] = True

    with app.app_context():
        db.create_all()  # Crée les tables dans la base de données de test

    with app.test_client() as client:
        yield client  # Fournit le client pour les tests

    with app.app_context():
        db.drop_all()  # Supprime les tables après les tests
