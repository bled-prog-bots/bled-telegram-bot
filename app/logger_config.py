import json
from logging.config import dictConfig


def setup(app_env: str) -> None:
    dict_config = json.load(
        open(f'logging.{app_env}.json', 'r', encoding='utf-8')
    )

    # Да, я знаю что есть fileConfig, но камон, json глазу приятнее и удобнее
    dictConfig(dict_config)
