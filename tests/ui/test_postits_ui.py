import pytest
from playwright.sync_api import Page, expect

@pytest.mark.ui
def test_create_postit(page, base_url):
    """Teste la création d'un post-it via l'interface utilisateur."""
    # Aller à la page d'accueil
    page.goto(f"{base_url}/")
    
    # Créer un utilisateur via l'API
    page.request.post(f"{base_url}/auth/register", data={
        "username": "testui",
        "email": "testui@example.com",
        "password": "testpassword"
    })
    
    # Se connecter via l'API
    page.request.post(f"{base_url}/auth/login", data={
        "identifier": "testui@example.com",
        "password": "testpassword"
    })
    
    # Accéder directement à la page des post-its après connexion
    page.goto(f"{base_url}/postits")

    # Ajoute cette ligne après avoir navigué vers la page des post-its
    page.screenshot(path="debug.png")

    # Ajoute ces lignes avant de cliquer sur le bouton d'ajout
    print("URL actuelle:", page.url)
    print("Bouton d'ajout visible:", page.is_visible("#add-postit"))
    
    # Ajouter un post-it
    page.click("#add-postit")
    
    # Attendre que le nouveau post-it apparaisse et utiliser locator directement
    page.wait_for_selector(".postit")
    
    # Utiliser des locators directement depuis la page
    title_field = page.locator(".postit").last.locator(".titre")
    content_field = page.locator(".postit").last.locator(".contenu")
    
    title_field.fill("Test automatisé")
    content_field.fill("Contenu de test")
    
    # Enregistrer
    page.locator(".postit").last.locator(".modifier-postit").click()
    
    # Attendre la notification
    page.wait_for_selector("#message-box.show")
    
    # Vérifier le contenu
    assert "Post-it sauvegardé" in page.locator("#message-box").text_content()