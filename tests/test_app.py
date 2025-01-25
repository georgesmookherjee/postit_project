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



