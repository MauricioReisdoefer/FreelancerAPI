from ..Extensions import db

class Proposal(db.Model):
    __tablename__ = 'proposal'

    id = db.Column(db.Integer, primary_key=True)
    preco = db.Column(db.Float)
    descricao = db.Column(db.Text, nullable=False)
    data_envio = db.Column(db.DateTime, default=db.func.current_timestamp())
    status = db.Column(db.String(20), default='pendente')

    projeto_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    projeto = db.relationship('Project', backref='proposals')

    freelancer_id = db.Column(db.Integer, db.ForeignKey('freelancer.id'), nullable=False)
    freelancer = db.relationship('Freelancer', backref='proposals')