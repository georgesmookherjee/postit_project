from app import create_app, db
import os

# Créer une instance de l'application Flask
app = create_app()

with app.app_context():
    db.create_all()
    print("Les tables ont été créées avec succès.") 

if __name__ == "__main__":
    # Utilise DATABASE_URL du .env
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    # Lancer l'application Flask en mode debug
    app.run(debug=True)

