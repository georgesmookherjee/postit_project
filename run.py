import os
from app import create_app

# Créer l'application Flask
app = create_app()

if __name__ == "__main__":
    # Charger la configuration de la base principale à partir du fichier .env
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Démarrer le serveur Flask
    app.run(debug=True)
