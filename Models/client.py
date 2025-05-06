from ..Extensions import db

class ClientProfile(db.Model):
    __tablename__ = 'client_profile'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    company_name = db.Column(db.String(100))
    bio = db.Column(db.Text)