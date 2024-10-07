import logging
from logging import handlers

logger = logging.getLogger("app_logger")
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "{asctime}.{msecs:03.0f}|{levelname}|{funcName}|{message}",
    datefmt="%Y-%m-%d %H:%M:%S",
    style="{",
)

handler = logging.handlers.TimedRotatingFileHandler(
    "../logs/system_log.log", when="midnight", interval=1
)
handler.setFormatter(formatter)

if not logger.hasHandlers():
    logger.addHandler(handler)
