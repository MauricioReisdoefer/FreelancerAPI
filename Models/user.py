from ..Extensions import db
from .freelancer import Freelancer
from .client import ClientProfile
import bcrypt
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    password_hash = db.Column(db.LargeBinary(60), nullable=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash)
    
    is_freelancer = db.Column(db.Boolean, default=False)
    freelancer_profile = db.relationship('Freelancer', backref='user', uselist=False)
    client_profile = db.relationship('ClientProfile', backref='user', uselist=False)
    
    @staticmethod
    def create_password(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def set_password(self, password):
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "is_freelancer": self.is_freelancer,
            "freelancer_profile": self.freelancer_profile.to_dict() if self.freelancer_profile else None,
            "client_profile": self.client_profile.to_dict() if self.client_profile else None
        }
