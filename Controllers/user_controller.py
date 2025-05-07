from ..Models import User
from ..Extensions import db
from flask import request, jsonify
from error import ValidationError, ConflictError, NotFoundError

def create_user(data):
    username = data.get("username")
    email = data.get('email')
    password = data.get('password')
    is_freelancer = data.get('is_freelancer', True)
    
    missing_fields = []
    if not username:
        missing_fields.append("username")
    if not email:
        missing_fields.append("email")
    if not password:
        missing_fields.append("password")

    if missing_fields:
        raise ValidationError(fields=missing_fields)

    if User.query.filter_by(email=email).first():
        raise ConflictError(fields=["email"], message="Email já está em uso.")
            
    password_hash = User.create_password(password)
    new_user = User(password_hash=password_hash, username=username, email=email, is_freelancer=is_freelancer)
        
    db.session.add(new_user)
    db.session.commit()
    
    return {'message':'Usuário Criado com Sucesso',
            'errors': None,
            'data': new_user.to_dict()
            }, 200
    
def get_all_users():
    all_users = User.query.all()
    return {
        'message': 'All Users Found',
        'errors': 'None',
        'data': [user.to_dict() for user in all_users]
    }, 200
    
def get_user_by_id(id):
    user = User.query.get(id)
    if not user:
        raise NotFoundError(field="id", value=id)
    return {
            'message': 'A user was found',
            'errors': 'None',
            'data': user.to_dict(),
        }, 200