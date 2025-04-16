def test_homepage(authenticated_client):
    """
    Teste que la page d'accueil s'affiche correctement.
    """
    response = authenticated_client.get('/')
    assert response.status_code == 200
    
    soup = BeautifulSoup(response.data, 'html.parser')
    assert soup.find('h1').text == "Mon Site de Post-its"  # Vérifie le titre h1

def test_postits_page(authenticated_client):
    """
    Teste que la page HTML des post-its s'affiche correctement.
    """
    response = authenticated_client.get('/postits')
    assert response.status_code == 200
    
    soup = BeautifulSoup(response.data, 'html.parser')
    assert soup.find('h2', id='postits-list').text == "Liste des Post-its"  # Vérifie le titre avec l'ID

import json
from bs4 import BeautifulSoup

def test_postit_display(authenticated_client):
    # 1️⃣ Ajouter un post-it via l'API REST
    postit_data = {"titre": "Test affichage", "contenu": "Vérif API"}
    response = authenticated_client.post("/api/postits", json=postit_data)
    assert response.status_code == 201  # Vérifier que l'ajout s'est bien fait

    # 2️⃣ Récupérer les post-its via l'API REST
    response = authenticated_client.get("/api/postits")
    assert response.status_code == 200  # Vérifier que la requête fonctionne

    postits = response.json  # Convertir en JSON
    postit_titles = [p["titre"] for p in postits]  # Extraire les titres

    # 3️⃣ Vérifier que le titre "Test affichage" est bien dans la liste
    assert "Test affichage" in postit_titles