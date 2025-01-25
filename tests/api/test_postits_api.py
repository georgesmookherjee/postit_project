def test_get_postits(client):
    """
    Teste la récupération des post-its via l'API.
    """
    response = client.get('/api/postits')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_create_postit(client):
    """
    Teste la création d'un post-it via l'API.
    """
    response = client.post('/api/postits/new', json={"titre": "Test API", "contenu": "Contenu API"})
    assert response.status_code == 201
    assert response.json['message'] == "Post-it créé avec succès"

def test_postit_validation(client):
    """
    Teste les validations des champs requis pour la création d'un post-it.
    """
    response = client.post('/api/postits/new', json={})
    assert response.status_code == 400
    assert response.json['message'] == "Les champs 'titre' et 'contenu' sont requis et ne doivent pas être vides."
