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
    
    Esse erro ocorre quando os dados fornecidos pelo usuário não foram corretamente preenchidos,
    estão ausentes ou estão em formato inválido, impedindo o processamento da requisição.

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
    
class ConflictError(AppError):
    """
    Classe de erro para conflitos de estado do recurso (HTTP 409).

    Esse erro ocorre quando a requisição é válida, mas não pode ser processada
    porque entraria em conflito com o estado atual do servidor. Exemplo típico:
    tentativa de criar um recurso já existente (como um email duplicado).

    :param fields: Dicionário com os campos que causaram o conflito.
    :param message: Mensagem principal do erro (padrão: 'Conflito com o estado atual do recurso').
    :param payload: Dados adicionais opcionais a serem incluídos na resposta de erro.
    """
    def __init__(self, fields=None, message="Conflito com o estado atual do recurso", payload=None):
        super().__init__(message, status_code=409, payload=payload)
        self.fields = fields

    def to_dict(self):
        data = super().to_dict()
        if self.fields:
            data['fields'] = self.fields
        return data
    
class NotFoundError(AppError):
    """
    Classe de erro para recursos não encontrados (HTTP 404).

    Esse erro ocorre quando um recurso solicitado (como um usuário, projeto ou item)
    não existe ou não pôde ser localizado com os critérios fornecidos.

    :param field: Campo usado na busca (ex: 'id', 'username').
    :param value: Valor buscado no campo (ex: 42, 'joao123').
    :param message: Mensagem principal do erro (padrão: 'Recurso não encontrado').
    :param payload: Dados adicionais opcionais a serem incluídos na resposta de erro.
    """
    def __init__(self, field=None, value=None, message="Recurso não encontrado", payload=None):
        super().__init__(message, status_code=404, payload=payload)
        self.field = field
        self.value = value

    def to_dict(self):
        data = super().to_dict()
        if self.field and self.value is not None:
            data['not_found'] = {self.field: self.value}
        return data
