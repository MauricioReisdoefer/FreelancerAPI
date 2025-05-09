from ..Extensions import db

class Project(db.Model):
    __tablename__ = 'project'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    data_criacao = db.Column(db.DateTime, default=db.func.current_timestamp())
    status = db.Column(db.String(20), default='aberto')

    client_id = db.Column(db.Integer, db.ForeignKey('client_profile.id'), nullable=False)
    cliente = db.relationship('ClientProfile', backref='projects')

    preco = db.Column(db.Float)
    prazo_dias = db.Column(db.Integer)
    
    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "data_criacao": self.data_criacao.isoformat() if self.data_criacao else None,
            "status": self.status,
            "client_id": self.client_id,
            "preco": self.preco,
            "prazo_dias": self.prazo_dias,
            "cliente": {
                "id": self.cliente.id,
                "company_name": self.cliente.nome,  
            } if self.cliente else None
        }