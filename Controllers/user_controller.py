from ..Models import User
from ..Extensions import db
from flask import request, jsonify
from error import ValidationError, ConflictError, NotFoundError, UnauthorizedError
import datetime
import jwt
from Extensions import get_token_env_var

def create_user(data):
    username = data.get("username")
    email = data.get('email')
    password = data.get('password')
    is_freelancer = data.get('is_freelancer', True)
    
    missing_fields = {}
    if not username:
        missing_fields["username"] = None
    if not email:
        missing_fields["email"] = None
    if not password:
        missing_fields["password"] = None
    if missing_fields:
        raise ValidationError(fields=missing_fields)

    if User.query.filter_by(email=email).first():
        raise ConflictError(fields={"email":email}, message="Email já está em uso.")
            
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
    
def update_user(data):
    user_id = data.get("user_id")
    user = User.query.get(user_id)
    if not user:
        raise NotFoundError(field="id", value=user_id)
    
    username = data.get("username")
    email = data.get('email')
    password = data.get('password')
    is_freelancer = data.get('is_freelancer')
    
    
    if username is not None:
        user.username = username
    if email is not None:
        user.email = email
    if password is not None:
        user.set_password(password)
    if is_freelancer is not None:
        user.is_freelancer = is_freelancer

    db.session.commit()
    return {
            'message': f'A user with id {user.id} was found and edited',
            'errors': 'None',
            'data': user.to_dict(),
        }, 200

def remove_user(user_id):
    user = User.query.get(user_id)
    if not user:
        raise NotFoundError(field="id", value=user_id)

    db.session.delete(user)
    db.session.commit()
    return {
            'message': f'A user with id {user.id} was found and deleted',
            'errors': 'None',
            'data': user.to_dict(),
        }, 200
    
def login_user(email, password):
    user = User.query.get(email=email)
    if user is None:
        raise NotFoundError(field="email", value=email)
    
    if not user.check_password(password):
        raise UnauthorizedError(payload=password)
    
    payload = {
        'sub': user.email, 
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  
    }
    
    SECRET_KEY = get_token_env_var()
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    return {
        'message': 'Login bem-sucedido!',
        'token': token
    }