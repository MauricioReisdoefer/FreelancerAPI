from user import User
from ..Extensions import db

class Freelancer(User):
    skills = db.Column(db.String(50), nullable=True)
    bio = db.Column(db.Text, nullable=True)  
    skills = db.Column(db.String(255), nullable=True) 
    availability = db.Column(db.String(50), default="Available")  
    location = db.Column(db.String(100), nullable=True)
    rating = db.Column(db.Float, default=0.0) 
    completed_projects = db.Column(db.Integer, default=0)