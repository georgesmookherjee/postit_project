import os
from dotenv import load_dotenv

# Chargement des variables d'environnement
load_dotenv()

class Config:
    """Configuration de base"""
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
    DEBUG = False
    TESTING = os.getenv("TESTING_MODE", "false").lower() == "true"  # Convertir en booléen
    
    # Valeur par défaut pour éviter l'erreur
    DEFAULT_DB_URL = "postgresql://post_it_georges:PostIt2025@postgres:5432/post_it"
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", DEFAULT_DB_URL)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    """Configuration pour le développement"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DEV_DATABASE_URL", Config.DEFAULT_DB_URL)

class TestingConfig(Config):
    """Configuration pour les tests"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv("TEST_DATABASE_URL", 
                                        "postgresql://post_it_test_georges:PostIttest2025@test_postgres:5432/post_it_test")

class ProductionConfig(Config):
    """Configuration pour la production"""
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", Config.DEFAULT_DB_URL)

# Sélection automatique de la config
APP_ENV = os.getenv("APP_ENV", "development")
TESTING_MODE = os.getenv("TESTING_MODE", "false").lower() == "true"

configurations = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig
}

# Choix de la configuration
if TESTING_MODE or APP_ENV == "testing":
    current_config = TestingConfig()
else:
    current_config = configurations.get(APP_ENV, DevelopmentConfig)()