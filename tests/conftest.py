import pytest
from app import create_app, db
import os
import time
import psycopg2

def wait_for_db():
    retries = 10  # Augmenter le nombre de tentatives
    while retries > 0:
        try:
            conn = psycopg2.connect(
                os.getenv('TEST_DATABASE_URL'),
                connect_timeout=5  # Timeout pour éviter les blocages
            )
            conn.close()
            print("✅ Base de données de test disponible !")
            return
        except psycopg2.OperationalError as e:
            print(f"Attente de la base de données de test... ({retries} tentatives restantes)")
            print(f"Erreur : {e}")
            retries -= 1
            time.sleep(5)  # Attendre 5 secondes avant de réessayer

    raise Exception("La base de données de test n'est pas prête après plusieurs tentatives !")


@pytest.fixture
def client():
    app = create_app(testing=True)  # Active le mode test
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('TEST_DATABASE_URL')  # Utilise la base PostgreSQL de test

    wait_for_db()  # Attente de PostgreSQL avant les tests

    with app.app_context():
        db.create_all()  # Crée les tables

    with app.test_client() as client:
        yield client

    with app.app_context():
        db.drop_all()  # Nettoie les tables après les tests
