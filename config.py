import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("DEV_DATABASE_URL")

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("PROD_DATABASE_URL")

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("TEST_DATABASE_URL")
    TESTING = True

# Dictionnaire pour choisir la bonne config
config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig
}

# Sélection automatique selon la variable FLASK_ENV
current_config = config.get(os.getenv("FLASK_ENV", "development"))()

# Ajoute cette ligne pour éviter l'erreur avec Alembic
DATABASE_URL = current_config.SQLALCHEMY_DATABASE_URI