from dotenv import load_dotenv
from error import AppError
import os

def get_token_env_var():
    load_dotenv()
    TOKEN_KEY = os.getenv("SECRET_KEY")
    if not TOKEN_KEY:
        raise AppError("Token de Validação Não Carregado")
    return TOKEN_KEY