from flask import Flask
from config import current_config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(current_config)

db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
