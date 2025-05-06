from ..Extensions import db

class Project(db.Model):
    __tablename__ = 'project'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    data_criacao = db.Column(db.DateTime, default=db.func.current_timestamp())
    status = db.Column(db.String(20), default='aberto')

    cliente_id = db.Column(db.Integer, db.ForeignKey('client_profile.id'), nullable=False)
    cliente = db.relationship('ClientProfile', backref='projetos')

    preco = db.Column(db.Float)
    prazo_dias = db.Column(db.Integer)
