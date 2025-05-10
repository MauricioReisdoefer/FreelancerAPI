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
    }, 200

def get_client_profile_by_user_id(user_id):
    user_client = ClientProfile.query.filter_by(user_id=user_id).first()
    if not user_client:
        raise NotFoundError(field={"user_id":user_id})
    return {
        "message": f"Client with user_id {user_id} was found",
        "errors":"None",
        "data":user_client.to_dict()
    }, 200

def get_all_clients():
    clients = ClientProfile.query.all()
    if not clients:
        raise NotFoundError()
    return {
        "message":"All clients were found",
        "errors":"None",
        "data":[client.to_dict() for client in clients]
    }, 200
    
def update_client(user_id, data):
    client = ClientProfile.query.filter_by(user_id=user_id).first()
    if not client:
        raise NotFoundError(field="user_id", value=user_id)

    company_name = data.get("company_name")
    bio = data.get("bio")

    if company_name is not None:
        client.company_name = company_name
    if bio is not None:
        client.bio = bio

    db.session.commit()

    return {
        "message": f"Client with user_id {user_id} updated successfully",
        "errors": "None",
        "data": client.to_dict()
    }, 200

def remove_client(user_id):
    client = ClientProfile.query.filter_by(user_id=user_id).first()
    if not client:
        raise NotFoundError(field="user_id", value=user_id)

    db.session.delete(client)
    db.session.commit()

    return {
        "message": f"Client with user_id {user_id} removed successfully",
        "errors": "None",
        "data":client.to_dict()
    }, 200
