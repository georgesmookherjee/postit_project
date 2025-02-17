from flask import Flask
from config import current_config
from flask_sqlalchemy import SQLAlchemy

# Importation des Blueprints
from app.routes import routes_app
from app.api.postits_api import api_bp  # Assure-toi que c'est bien le bon chemin

app = Flask(__name__)
app.config.from_object(current_config)

db = SQLAlchemy(app)

# Enregistrement des Blueprints
app.register_blueprint(routes_app)
app.register_blueprint(api_bp, url_prefix="/api")  # Si tes routes API sont sous /api

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
