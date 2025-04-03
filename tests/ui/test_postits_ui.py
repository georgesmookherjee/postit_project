import pytest
from playwright.sync_api import Page, expect


@pytest.mark.ui
def test_create_postit(page: Page, base_url):
    """Teste la création d'un post-it via l'interface utilisateur."""
    # Connecter l'utilisateur
    page.goto(f"{base_url}/")
    page.fill("#email", "test@example.com")
    page.fill("#password", "password123")
    page.click("#login-btn")
    
    # Attendre que la redirection se fasse
    page.wait_for_url(f"{base_url}/postits")
    
    # Attendre que la redirection se fasse
    page.wait_for_url("http://localhost:5000/postits")
    
    # Ajouter un post-it
    page.click("#add-postit")
    
    # Attendre que le nouveau post-it apparaisse
    page.wait_for_selector(".postit")
    
    # Modifier le contenu
    new_postit = page.locator(".postit").last
    new_postit.locator(".titre").fill("Test automatisé")
    new_postit.locator(".contenu").fill("Contenu de test")
    
    # Enregistrer
    new_postit.locator(".modifier-postit").click()
    
    # Vérifier que la notification apparaît
    expect(page.locator("#message-box")).to_have_text("Post-it sauvegardé !")