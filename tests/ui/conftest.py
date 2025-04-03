# Dans tests/ui/conftest.py ou dans ton conftest.py principal

import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    """Configure le lancement du navigateur pour les tests."""
    return {
        **browser_type_launch_args,
        "headless": True,  # true pour exécuter sans interface, false pour voir le navigateur
    }

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Configure le contexte du navigateur."""
    return {
        **browser_context_args,
        "viewport": {
            "width": 1280,
            "height": 720,
        },
    }

@pytest.fixture
def base_url():
    """URL de base pour les tests."""
    return "http://flask_app:5000"  # URL du service Flask dans Docker Compose