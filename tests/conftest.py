import pytest
from app import create_app, db
import os
import time
import psycopg2

# Forcer le mode test
os.environ["TESTING_MODE"] = "true"

@pytest.fixture
def client():
    app = create_app(testing=True)  # Active le mode test
    database_url = os.getenv("TEST_DATABASE_URL")
    app.config["SQLALCHEMY_DATABASE_URI"] = database_url

    with app.app_context():
        db.create_all()  # Créer les tables pour le test
        yield app.test_client()
        db.session.remove()  # <- s'assurer qu'aucune connexion ne reste ouverte
        db.drop_all()  # Nettoyer après les tests
        print("Base de test nettoyée")  # Vérification si cette ligne s'affiche après chaque test

# def wait_for_db():
#     retries = 2  # Ajuster le nombre de tentatives
#     while retries > 0:
#         try:
#             conn = psycopg2.connect(
#                 os.getenv('TEST_DATABASE_URL'),
#                 connect_timeout=3  # Timeout pour éviter les blocages
#             )
#             conn.close()
#             return
#         except psycopg2.OperationalError as e:
#             print(f"Attente de la base de données de test... ({retries} tentatives restantes)")
#             print(f"Erreur : {e}")
#             retries -= 1
#             time.sleep(2)  # ajuster le nombre de secondes avant de réessayer

#     raise Exception("La base de données de test n'est pas prête après plusieurs tentatives !")
