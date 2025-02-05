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

def test_update_postit(client):
    """
    Teste la mise à jour d'un post-it existant.
    """
    response = client.post('/api/postits/new', json={"titre": "Ancien titre", "contenu": "Ancien contenu"})
    assert response.status_code == 201
    postit_id = response.json["postit"]["id"]  # 🔹 Correction ici

    response = client.put(f'/api/postits/{postit_id}', json={"titre": "Nouveau titre", "contenu": "Nouveau contenu"})
    assert response.status_code == 200
    assert response.json['message'] == "Post-it mis à jour avec succès"
    assert response.json['postit']['titre'] == "Nouveau titre"
    assert response.json['postit']['contenu'] == "Nouveau contenu"


def test_update_postit_not_found(client):
    """
    Teste la mise à jour d'un post-it inexistant.
    """
    response = client.put('/api/postits/9999', json={"titre": "Test", "contenu": "Test"})
    assert response.status_code == 404
    assert response.json['message'] == "Post-it non trouvé"

def test_update_postit_invalid_data(client):
    """
    Teste la mise à jour avec des données invalides.
    """
    # Création d'un post-it
    response = client.post('/api/postits/new', json={"titre": "Titre", "contenu": "Contenu"})
    assert response.status_code == 201
    postit_id = response.json.get("postit", {}).get("id")

    # Envoi d'une requête sans données
    response = client.put(f'/api/postits/{postit_id}', json={})
    assert response.status_code == 400
    assert response.json['message'] == "Requête invalide, envoi de données requis."

def test_delete_postit(client):
    """
    Teste la suppression d'un post-it existant.
    """
    response = client.post('/api/postits/new', json={"titre": "Test Delete", "contenu": "Contenu Delete"})
    assert response.status_code == 201
    postit_id = response.json["postit"]["id"]  # 🔹 Correction ici

    response = client.delete(f'/api/postits/{postit_id}')
    assert response.status_code == 200
    assert response.json["message"] == "Post-it supprimé avec succès"


def test_delete_postit_not_found(client):
    """
    Teste la suppression d'un post-it inexistant.
    """
    response = client.delete('/api/postits/99999')  # ID qui n'existe pas
    assert response.status_code == 404
    assert response.json["message"] == "Post-it non trouvé"
