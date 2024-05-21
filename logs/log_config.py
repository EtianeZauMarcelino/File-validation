from loguru import logger
from sys import stderr
from functools import wraps
from datetime import datetime

date = datetime.today().date()

# Removendo os handlers existentes para evitar duplicação
logger.remove()

# Configuração do logger para stderr
logger.add(
                sink=stderr,
                format="{time} <r>{level}</r> <g>{message}</g> {file}",
                level="INFO"
            )

# Configuração do logger para arquivo de log
logger.add(
                fr"logs/execution_log_{date}.log",
                format="{time} {level} | {line: <3} | {message} {file}",
                level="INFO"
            )

def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Chamando função '{func.__name__}' com args {args} e kwargs {kwargs}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"Função '{func.__name__}' retornou python object type {type(result)}")
            logger.info(f"Função '{func.__name__}' retornou {result}")
            return result
        except Exception as e:
            logger.exception(f"Exceção capturada em '{func.__name__}': {e}")
            raise  # Re-lança a exceção para não alterar o comportamento da função decorada
    return wrapper