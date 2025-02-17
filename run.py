from flask import Flask
from config import current_config
from flask_sqlalchemy import SQLAlchemy
import os
from app.models import db
from dotenv import load_dotenv
from flask_migrate import Migrate

# Charger les variables d'environnement depuis .env
load_dotenv()

# Spécifier le dossier templates explicitement
app = Flask(__name__, template_folder=os.path.join(os.getcwd(), "app", "templates"))

app.config.from_object(current_config)

db.init_app(app)  #initialise la base de données
migrate = Migrate(app, db)

# Importer et enregistrer les Blueprints
from app.routes import routes_app
from app.api.postits_api import api_bp  

app.register_blueprint(routes_app)
app.register_blueprint(api_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
