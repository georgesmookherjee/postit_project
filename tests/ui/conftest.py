import os
import pytest
from playwright.sync_api import sync_playwright

# Configurer la marque UI pour éviter l'avertissement
def pytest_configure(config):
    config.addinivalue_line("markers", "ui: mark test as a UI test")

@pytest.fixture(scope="session")
def browser_type_launch_args():
    """Configure le lancement du navigateur pour les tests."""
    return {
        "headless": True,
        "args": [
            "--no-sandbox",
            "--disable-dev-shm-usage"  # Recommandé pour Docker
        ]
    }

@pytest.fixture(scope="function")
def page(browser):
    """Crée une nouvelle page pour chaque test."""
    page = browser.new_page()
    yield page
    page.close()

@pytest.fixture(scope="session")
def base_url():
    """URL de base pour les tests."""
    # Utiliser la variable d'environnement BASE_URL si elle existe
    return os.environ.get('BASE_URL', 'http://flask_app:5000')