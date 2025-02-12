from app import create_app, db

# Création de l'application Flask
app = create_app()

# Vérifie que la base de données est bien initialisée
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
