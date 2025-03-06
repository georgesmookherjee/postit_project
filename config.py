import os

class Config:
    """Configuration de base, chargée par défaut"""
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    """Configuration pour le développement"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DEV_DATABASE_URL")

class TestingConfig(Config):
    """Configuration pour les tests"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv("TEST_DATABASE_URL")

class ProductionConfig(Config):
    """Configuration pour la production"""
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

# Sélection automatique de la config en fonction de l'environnement
configurations = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig
}

FLASK_ENV = os.getenv("FLASK_ENV", "development")
current_config = configurations.get(os.getenv("FLASK_ENV", "development"))