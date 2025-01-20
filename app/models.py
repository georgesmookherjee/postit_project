from . import db

class PostIt(db.Model):
    __tablename__ = 'postits'

    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(100), nullable=False)
    contenu = db.Column(db.Text, nullable=False)
    date_creation = db.Column(db.DateTime, server_default=db.func.now())
