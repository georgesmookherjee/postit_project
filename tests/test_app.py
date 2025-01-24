import pytest
from app import create_app, db  # Import absolu basé sur la structure du projet


@pytest.fixture
def client():

    # Créer une instance de l'application Flask pour les tests
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/post_it_test'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Vérification stricte pour éviter les erreurs
    if "post_it_test" not in app.config['SQLALCHEMY_DATABASE_URI']:
        raise RuntimeError("Tentative de modification de la base principale ! Utilisez la base de tests.")

    # Ajout du print pour vérifier la base utilisée
    print("Base utilisée pour les tests :", app.config['SQLALCHEMY_DATABASE_URI'])

    # Initialiser la base de données
    with app.app_context():
        db.create_all()  # Crée toutes les tables définies dans models.py

    with app.test_client() as client:
        yield client  # Fournit un client de test
    # Nettoyer la base après les tests
    with app.app_context():
        db.session.remove()
        db.drop_all()

def test_homepage(client):
    # Tester la route d'accueil
    response = client.get('/')
    assert response.status_code == 200

def test_créer_postit(client):
    # Simuler une requête POST vers la route /add_postit
    response = client.post('/créer_postit', json={"titre": "Test Post-It", "contenu": "Ceci est un test"})
    
    # Vérifie que la réponse HTTP est 200 (OK)
    assert response.status_code == 201
    
    # Vérifie que la réponse contient un message de succès
    assert response.json['message'] == "Post-it créé avec succès" # Ajuste ce message si nécessaire

def test_postit_saved_in_database(client):
    """
    Teste si la route /créer_postit permet de créer un Post-It
    et retourne le bon code de statut et message.
    """
        
    # Simuler une requête POST pour créer un Post-It
    client.post('/créer_postit', json={"titre": "Test DB", "contenu": "Contenu de test"})

    # Vérifier que les données sont bien enregistrées
    from app.models import PostIt  # Importe le modèle PostIt
    with client.application.app_context():
        postit = PostIt.query.filter_by(titre="Test DB").first()
        assert postit is not None  # Vérifie que le Post-It existe
        assert postit.contenu == "Contenu de test"  # Vérifie le contenu du Post-It

