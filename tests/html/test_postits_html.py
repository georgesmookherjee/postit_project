def test_homepage(client):
    """
    Teste que la page d'accueil s'affiche correctement.
    """
    response = client.get('/')
    print(response.data)
    assert response.status_code == 200
    assert b"Bienvenue sur votre site de Post-Its" in response.data

def test_postits_page(client):
    """
    Teste que la page HTML des post-its s'affiche correctement.
    """
    response = client.get('/postits')
    print("Contenu de la réponse:", response.data)
    assert response.status_code == 200
    assert b"Liste des Post-Its" in response.data
