# Built-In
from logging import Formatter, Logger
from os import environ
import logging

logging.logProcesses = False
logging.logThreads = False
logging.logMultiprocessing = False


def get_log_formatter() -> Formatter:
    return logging.Formatter(
        "%(asctime)s [%(levelname)s] (%(name)s) -> %(message)s", "%Y-%m-%dT%H:%M:%S%z"
    )


def set_logger(
    name: str = "default",
    level: int = None,
    formatter: Formatter = get_log_formatter(),
) -> Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level or int(environ.get("LOG_LEVEL", logging.DEBUG)))

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    return logger
