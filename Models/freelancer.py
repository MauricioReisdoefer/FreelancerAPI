from ..Extensions import db
from .proposal import Proposal

class Freelancer(db.Model):
    __tablename__ = 'freelancer'

    id = db.Column(db.Integer, primary_key=True)  # Estava faltando ID
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    skills = db.Column(db.String(255), nullable=True)
    bio = db.Column(db.Text, nullable=True)
    availability = db.Column(db.String(50), default="Available")
    location = db.Column(db.String(100), nullable=True)
    rating = db.Column(db.Float, default=0.0)
    completed_projects = db.Column(db.Integer, default=0)
    
    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "skills": self.skills,
            "bio": self.bio,
            "availability": self.availability,
            "location": self.location,
            "rating": self.rating,
            "completed_projects": self.completed_projects
        }