import logging
import sys
from pathlib import Path

from django.conf import settings
from loguru import logger

from libs.logging.handlers import LoguruHandler


def setup_logging():
    """
    Configure logging for Django using Loguru.
    """
    logger.remove()
    log_dir = settings.LOG_DIR

    # Configure loguru
    config = {
        "handlers": [
            {
                "sink": sys.stdout,
                "level": "INFO",
                "format": "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
            },
            {
                "sink": Path(settings.LOG_DIR) / "app.log",
                "level": "INFO",
                "rotation": "10 MB",
                "retention": "1 week",
                "format": "{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {name}:{function}:{line} - {message}",
            },
        ],
    }

    logging.basicConfig(handlers=[LoguruHandler()], level=0, force=True)
    logger.configure(**config)
