from ..Models import Project, ClientProfile
from ..Extensions import db
from flask import request, jsonify
from error import ValidationError, ConflictError, NotFoundError, UnauthorizedError

def create_project(data):
    client_id = data.get("client_id")
    if not client_id:
        raise ValidationError(fields=[client_id])
    client = ClientProfile.query.filter_by(id=client_id).first()
    if not client:
        raise NotFoundError(field="client_id", value=client_id)
    
    title = data.get("titulo")
    descricao = data.get("descricao")
    preco = data.get("preco")
    prazo_dias = data.get("prazo_dias")
    
    missing_fields = []
    if not title: 
        missing_fields.append(title)
    if not descricao: 
        missing_fields.append(descricao)
    if not preco: 
        missing_fields.append(preco)
    if not prazo_dias:
        missing_fields.append(prazo_dias)
    if missing_fields:
        raise ValidationError(fields=missing_fields)
    
    new_project = Project(
        titulo = title,
        descricao = descricao,
        client_id = client_id,
        preco = preco,
        prazo_dias = prazo_dias
    )
    
    db.session.add(new_project)
    db.session.commit()
    return {
        "message":f"Projeto do Cliente com ID {client_id} criado",
        "errors":"None",
        "data":new_project.to_dict()
    }, 200
    
def find_project_by_id(id):
    project = Project.query.filter_by(id=id).first()
    if not project:
        raise NotFoundError(field="ID", value=id)
    return {
        "message":"Projeto com ID {id} Encontrado",
        "errors":"None",
        "data":project.to_dict()
    }, 200
    
def find_all_client_projects(client_id):
    projects = Project.query.filter_by(client_id=client_id).all()
    if not projects:
        raise NotFoundError(field="ClientID", value=client_id)
    return [project.to_dict() for project in projects]

def find_all_projects():
    projects = Project.query.all()
    if not projects:
        raise NotFoundError()
    return [project.to_dict() for project in projects]