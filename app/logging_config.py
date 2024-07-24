import logging


def setup(log_format: str, level: str = 'INFO'):
    logging.basicConfig(
        level=level,
        format=log_format
    )
