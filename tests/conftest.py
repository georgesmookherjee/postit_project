import pytest
from app import create_app, db

@pytest.fixture
def client():
    app = create_app(testing=True)  # Active le mode test
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Utilise une base SQLite en mémoire
    with app.app_context():
        db.create_all()  # Crée les tables
    with app.test_client() as client:
        yield client
    with app.app_context():
        db.drop_all()  # Nettoie les tables après les tests
