class AppError(Exception):
    def __init__(self, message: str, status_code: int = 400, payload: dict = None):
        """
        Classe base para erros da aplicação.

        :param message: Mensagem de erro para exibir ou logar.
        :param status_code: Código HTTP associado ao erro (ex: 400, 404, 500...).
        :param payload: Dados extras opcionais para o erro.
        """
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.payload = payload or {}

    def to_dict(self):
        rv = dict(self.payload)
        rv['error'] = self.message
        rv['status_code'] = self.status_code
        return rv
    
class ValidationError(AppError):
    """
    Classe de erro para erros de validação de dados de entrada.

    :parameter fields: Dicionário com os campos que estão ausentes, inválidos ou com erro.
    :parameter message: Mensagem principal do erro (padrão: 'Dados inválidos ou incompletos').
    :parameter payload: Dados adicionais opcionais a serem incluídos na resposta de erro.
    """
    def __init__(self, fields=None, message="Dados inválidos ou incompletos", payload=None):
        super().__init__(message, status_code=400, payload=payload)
        self.fields = fields
        
    def to_dict(self):
        data = super().to_dict()
        if self.fields:
            data['fields'] = self.fields
        return data