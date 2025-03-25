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

import json
from bs4 import BeautifulSoup

def test_postit_display(client):
    # 1️⃣ Ajouter un post-it via l'API REST
    postit_data = {"titre": "Test affichage", "contenu": "Vérif API"}
    response = client.post("/api/postits", json=postit_data)
    assert response.status_code == 201  # Vérifier que l'ajout s'est bien fait

    # 2️⃣ Récupérer les post-its via l'API REST
    response = client.get("/api/postits")
    assert response.status_code == 200  # Vérifier que la requête fonctionne

    postits = response.json  # Convertir en JSON
    postit_titles = [p["titre"] for p in postits]  # Extraire les titres

    # 3️⃣ Vérifier que le titre "Test affichage" est bien dans la liste
    assert "Test affichage" in postit_titles