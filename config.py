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

print(f"🔍 Configuration chargée: {current_config.__class__.__name__}")
print(f"🔍 SQLALCHEMY_DATABASE_URI: {current_config.SQLALCHEMY_DATABASE_URI}")
print(f"🔍 TESTING_MODE = {TESTING_MODE}")
print(f"🔍 APP_ENV = {APP_ENV}")
