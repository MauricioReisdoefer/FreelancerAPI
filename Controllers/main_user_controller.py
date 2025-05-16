from .user_controller import create_user, get_user_by_id, get_all_users, update_user, remove_user, login_user
from .client_controller import create_client, get_client_profile_by_user_id, get_all_clients, remove_client, update_client
from .freelancer_controller import create_freelancer, get_freelancer_profile, get_all_freelancer_profiles, remove_freelancer, update_freelancer
from ..Extensions import db
from flask import request, jsonify
from error import ValidationError, ConflictError, NotFoundError, UnauthorizedError

def create_complete_user(data):
    user_response, status_code = create_user(data)
    user_data = user_response["data"]
    user_id = user_data["id"]
    is_freelancer = user_data["is_freelancer"]

    if is_freelancer:
        freelancer_data = {
            "user_id": user_id,
            "skills": data.get("skills"),
            "bio": data.get("bio"),
            "availability": data.get("availability"),
            "location": data.get("location"),
            "rating": data.get("rating"),
            "completed_projects": data.get("completed_projects")
        }
        profile_response, status = create_freelancer(freelancer_data)
    else:
        client_data = {
            "user_id": user_id,
            "company_name": data.get("company_name"),
            "bio": data.get("bio")
        }
        profile_response, status = create_client(client_data)

    return {
        "message": "Usuário completo criado com sucesso",
        "errors": None,
        "data": {
            "user_data": user_data,
            "profile_data": profile_response.get("data")
        }
    }, status_code

def get_complete_user(id):
    user, status_code = get_user_by_id(id=id)
    if user.get("data").get("is_freelancer") == True:
        profile, status = get_freelancer_profile(user_id=id)
    else:
        profile, status = get_client_profile_by_user_id(user_id=id)
    return {
        "message": "Usuário encontrado com sucesso",
        "errors": None,
       "data": {
            "user_data": user.get("data"),
            "profile_data": profile.get("data")
        }
    }, 200
    
def update_complete_user(data):
    user, status_code = update_user(data.get("user"))
    if user.get("data").get("is_freelancer") == True:
        profile, stauts = update_freelancer(data.get("profile"))
    else:
        profile, status = update_client(data.get("profile"))
    return {
        "message":"Usuário modificado com sucesso",
        "errors":None,
        "data":{
            "user_data":user.get("data"),
            "profile_data":profile.get("data")
        }
    }

def remove_complete_user(id):
    user_response, status_code = get_user_by_id(id)
    
    user_data = user_response.get("data")
    is_freelancer = user_data.get("is_freelancer")

    if is_freelancer:
        profile_response, status = remove_freelancer(user_id=id)
    else:
        profile_response, status = remove_client(user_id=id)

    user_deleted, user_status = remove_user(id)

    return {
        "message": "Usuário completo removido com sucesso",
        "errors": None,
        "data": {
            "user_data": user_deleted.get("data"),
            "profile_data": profile_response.get("data")
        }
    }, 200