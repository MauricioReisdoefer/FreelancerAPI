from ..Models import Freelancer
from ..Extensions import db
from flask import request, jsonify
from error import ValidationError, ConflictError, NotFoundError, UnauthorizedError

def create_freelancer(data):
    user_id = data.get("user_id")
    if not user_id:
        raise ValidationError(fields=user_id)
    
    skills = data.get("skills")
    bio = data.get("bio")
    avaliability = data.get("availability")
    location = data.get("location")
    rating = data.get("rating")
    completed_projects = data.get("completed_projects")
    
    new_freelancer = Freelancer(user_id=user_id,
                                skills=skills,
                                bio=bio,
                                avaliability=avaliability, 
                                location=location,
                                rating=rating,
                                completed_projects=completed_projects
                                )
    db.session.add(new_freelancer)
    db.session.commit()
    return {
        "message":"Freelancer criado com Sucesso",
        "errors":"None",
        "data":new_freelancer.to_dict()
    }

def get_freelancer_profile(user_id):
    user_freelancer = Freelancer.query.filter_by(user_id=user_id).first()
    if not user_freelancer:
        raise NotFoundError(field=user_id)
    return {
        "message":f"Freelancer com user_id {user_id} Encontrado com Sucesso",
        "errors":"None",
        "data":user_freelancer.to_dict()
    }
    
def get_all_freelancer_profiles():
    all_freelancers = Freelancer.query.all()
    if not all_freelancers:
        raise NotFoundError()
    return {
        "message":"All Freelancers Found",
        "errors":"None",
        "data":[frelan.to_dict() for frelan in all_freelancers]
    }