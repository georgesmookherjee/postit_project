import os

class Config:
    """Configuration de base"""
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
    DEBUG = False
    TESTING = os.getenv("TESTING_MODE", "false").lower() == "true"  # Convertir en booléen
    SQLALCHEMY_DATABASE_URI = os.getenv("DEV_DATABASE_URL")  # Base de dev par défaut

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

# Sélection automatique de la config
APP_ENV = os.getenv("APP_ENV", "development")
TESTING_MODE = os.getenv("TESTING_MODE", "false").lower() == "true"

if TESTING_MODE:
    current_config = TestingConfig()
else:
    configurations = {
        "development": DevelopmentConfig,
        "testing": TestingConfig,
        "production": ProductionConfig
    }
    current_config = configurations.get(APP_ENV, DevelopmentConfig)()

