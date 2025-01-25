import pytest
from app import create_app, db

@pytest.fixture
def client():
    app = create_app(testing=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.app_context():
        db.create_all()  # Crée les tables pour les tests
    with app.test_client() as client:
        yield client
    with app.app_context():
        db.drop_all()  # Supprime les tables après les tests
