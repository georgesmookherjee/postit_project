from flask import Flask
from config import current_config
from flask_sqlalchemy import SQLAlchemy
import os

# Spécifier le dossier templates explicitement
app = Flask(__name__, template_folder=os.path.join(os.getcwd(), "app", "templates"))

app.config.from_object(current_config)

db = SQLAlchemy(app)

# Importer et enregistrer les Blueprints
from app.routes import routes_app
from app.api.postits_api import api_bp  

app.register_blueprint(routes_app)
app.register_blueprint(api_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
