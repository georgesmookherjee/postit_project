from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class PostIt(db.Model):
    __tablename__ = 'postits'

    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(25), nullable=False)
    contenu = db.Column(db.Text, nullable=False)
    date_creation = db.Column(db.DateTime, server_default=db.func.now())

    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # user = db.relationship('User', backref=db.backref('postits', lazy=True))

    def to_dict(self):
        return {
            "id": self.id,
            "titre": self.titre,
            "contenu": self.contenu,
            # "created_at": self.date_creation.strftime("%Y-%m-%d %H:%M:%S")  # Optionnel
        }

# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password_hash = db.Column(db.String(256), nullable=False)
    
#     # Méthodes pour gérer les mots de passe
#     def set_password(self, password):
#         self.password_hash = generate_password_hash(password)
    
#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)