import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(log_path: str = "logs/pipeline.log") -> logging.Logger:
    os.makedirs(os.path.dirname(log_path), exist_ok=True)

    logger = logging.getLogger("pipeline")
    logger.setLevel(logging.INFO)

    # Evita duplicar handlers se você rodar o programa mais de uma vez no mesmo processo
    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Log no console (para você ver ao rodar)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # Log em arquivo com rotação (para histórico e auditoria)
    file_handler = RotatingFileHandler(
        log_path,
        maxBytes=500_000,
        backupCount=3,
        encoding="utf-8"
    )
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger

# Por que fiz assim e o que buscamos:
# Console + arquivo: console retorna feedback rápido; arquivo cria histórico e é essencial pra auditoria e debugging pós-mortem.;
# RotatingFileHandler: evita log crescer infinitamente e virar problema de disco, pois limita o tamanho do arquivo e mantém backups;
# formatter padronizado: logs sem padrão viram caos; com padrão, você consegue filtrar e debugar, mesmo que o log seja grande;
# if logger.handlers: previne o bug clássico de “duplicar log” quando o script é executado mais de uma vez no mesmo runtime.