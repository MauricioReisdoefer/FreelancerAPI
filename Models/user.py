from ..Extensions import db
import bcrypt
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    password_hash = db.Column(db.LargeBinary(60), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    def set_password(self, password):
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash)
    
    is_freelancer = db.Column(db.Boolean, default=False)
    freelancer_profile = db.relationship('Freelancer', backref='user', uselist=False)
    client_profile = db.relationship('ClientProfile', backref='user', uselist=False)