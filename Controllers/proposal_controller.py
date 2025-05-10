from ..Models import Proposal, Project, Freelancer
from ..Extensions import db
from flask import request, jsonify
from error import ValidationError, ConflictError, NotFoundError, UnauthorizedError

def create_proposal(data):
    freelancer_id = data.get("freelancer_id")
    project_id = data.get("project_id")
    preco = data.get("preco")
    descricao = data.get("descricao")
    
    missing_fields = []
    if not freelancer_id:
        missing_fields.append("freelancer_id")
    if not project_id:
        missing_fields.append("project_id")
    if not preco:
        missing_fields.append("preco")
    if not descricao:
        missing_fields.append("descricao")
    
    if missing_fields:
        raise ValidationError(fields=missing_fields)
    
    freelancer = Freelancer.query.filter_by(id=freelancer_id).first()
    if not freelancer:
        raise NotFoundError(field="freelancer_id", value=freelancer_id)
        
    project = Project.query.filter_by(id=project_id).first()
    if not project:
        raise NotFoundError(field="project_id", value=project_id)
    
    new_proposal = Proposal(
        freelancer_id=freelancer_id,
        projeto_id=project_id,
        preco=preco,
        descricao=descricao
    )
    
    db.session.add(new_proposal)
    db.session.commit()
    
    return {
        "message": f"Proposta criada com sucesso para o projeto {project_id}",
        "errors": "None",
        "data": new_proposal.to_dict()
    }, 200
    
def get_all_freelancer_proposals(freelancer_id):
    proposals = Proposal.query.filter_by(freelancer_id=freelancer_id).all()
    if not proposals:
        raise NotFoundError(field="freelancer_id", value=freelancer_id)
    
    return {
        "message": f"{len(proposals)} propostas encontradas para o freelancer {freelancer_id}",
        "errors": "None",
        "data": [proposal.to_dict() for proposal in proposals]
    }, 200

def get_all_project_proposals(project_id):
    proposals = Proposal.query.filter_by(projeto_id=project_id).all()
    if not proposals:
        raise NotFoundError(field="project_id", value=project_id)
    
    return {
        "message": f"{len(proposals)} propostas encontradas para o projeto {project_id}",
        "errors": "None",
        "data": [proposal.to_dict() for proposal in proposals]
    }, 200
    
def get_proposal_by_id(proposal_id):
    proposal = Proposal.query.filter_by(id=proposal_id).first()
    if not proposal:
        raise NotFoundError(field="proposal_id", value=proposal_id)
    
    return {
        "message": f"Proposta com ID {proposal_id} encontrada",
        "errors": "None",
        "data": proposal.to_dict()
    }, 200
    
def update_proposal(proposal_id, data):
    proposal = Proposal.query.filter_by(id=proposal_id).first()
    if not proposal:
        raise NotFoundError(field="proposal_id", value=proposal_id)

    if proposal.status != 'pendente':
        raise ConflictError(detail="Propostas só podem ser editadas enquanto estão pendentes.")

    preco = data.get("preco")
    descricao = data.get("descricao")

    if preco is not None:
        proposal.preco = preco
    if descricao is not None:
        proposal.descricao = descricao

    db.session.commit()

    return {
        "message": f"Proposta {proposal_id} atualizada com sucesso.",
        "errors": "None",
        "data": proposal.to_dict()
    }, 200
    
def remove_proposal(proposal_id):
    proposal = Proposal.query.filter_by(id=proposal_id).first()
    if not proposal:
        raise NotFoundError(field="proposal_id", value=proposal_id)

    db.session.delete(proposal)
    db.session.commit()

    return {
        "message": f"Proposta {proposal_id} removida com sucesso.",
        "errors": "None",
        "data": proposal.to_dict()
    }, 200
