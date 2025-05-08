from ..Models import ClientProfile
from ..Extensions import db
from flask import request, jsonify
from error import ValidationError, ConflictError, NotFoundError, UnauthorizedError

def create_client(data):
    user_id = data.get("user_id")
    if not user_id:
        raise NotFoundError(field={"user_id":user_id})

    company_name = data.get("company_name")
    if not company_name:
        raise ValidationError(fields={"comany_name":company_name})
    
    bio = data.get("bio")
    
    new_client = ClientProfile(
        user_id=user_id,
        company_name=company_name,
        bio=bio
    )
    db.session.add(new_client)
    db.session.commit()
    return {
        "message":f"Client with user_id {user_id} sucefully created",
        "errors":"None",
        "data":new_client.to_dict()
    }

def get_client_profile(user_id):
    user_client = ClientProfile.query.filter_by(user_id=user_id).first()
    if not user_client:
        raise NotFoundError(field={"user_id":user_id})