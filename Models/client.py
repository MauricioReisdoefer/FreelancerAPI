from ..Extensions import db

class ClientProfile(db.Model):
    __tablename__ = 'client_profile'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    company_name = db.Column(db.String(100))
    bio = db.Column(db.Text, nullable=False)
    
    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "company_name": self.company_name,
            "bio": self.bio,
        }
        