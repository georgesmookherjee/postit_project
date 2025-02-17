from . import db
from flask import current_app

class PostIt(db.Model):
    __tablename__ = 'postits'

    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(100), nullable=False)
    contenu = db.Column(db.Text, nullable=False)
    date_creation = db.Column(db.DateTime, server_default=db.func.now())

    def to_dict(self):
        return {
            "id": self.id,
            "titre": self.titre,
            "contenu": self.contenu,
            # "created_at": self.date_creation.strftime("%Y-%m-%d %H:%M:%S")  # Optionnel
        }
