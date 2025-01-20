from app import create_app

# Créer une instance de l'application Flask
app = create_app()

if __name__ == "__main__":
    # Lancer l'application Flask en mode debug
    app.run(debug=True)