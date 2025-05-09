from ..Models import Freelancer
from ..Extensions import db
from flask import request, jsonify
from error import ValidationError, NotFoundError

def create_freelancer(data):
    user_id = data.get("user_id")
    if not user_id:
        raise ValidationError(fields={"user_id":user_id})
    
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
        raise NotFoundError(field="user_id", value=user_id)
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
    
def update_freelancer(user_id, data):
    freelancer = Freelancer.query.filter_by(user_id=user_id).first()
    if not freelancer:
        raise NotFoundError(field="user_id", value=user_id)

    if "skills" in data:
        freelancer.skills = data["skills"]
    if "bio" in data:
        freelancer.bio = data["bio"]
    if "availability" in data:
        freelancer.avaliability = data["availability"]
    if "location" in data:
        freelancer.location = data["location"]
    if "rating" in data:
        freelancer.rating = data["rating"]
    if "completed_projects" in data:
        freelancer.completed_projects = data["completed_projects"]

    db.session.commit()

    return {
        "message": f"Freelancer com user_id {user_id} atualizado com sucesso",
        "errors": "None",
        "data": freelancer.to_dict()
    }

def remove_freelancer(user_id):
    freelancer = Freelancer.query.filter_by(user_id=user_id).first()
    if not freelancer:
        raise NotFoundError(field="user_id", value=user_id)

    db.session.delete(freelancer)
    db.session.commit()

    return {
        "message": f"Freelancer com user_id {user_id} removido com sucesso",
        "errors": "None",
        "data": None
    }