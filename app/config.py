import os
import logging
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv, find_dotenv

__all__ = [
    'get_config',
    'AppConfig',
    'BotConfig',
    'ChatGptConfig',
    'SqliteConfig',
    'LoggingConfig',
    'AppConfig',
    'Config'
]


@dataclass
class AppConfig:
    bled_chat_id: str


@dataclass
class BotConfig:
    token: str


@dataclass
class ChatGptConfig:
    model: str
    token: str
    chat_context: str


@dataclass
class SqliteConfig:
    filepath: Path
    filename: Path


@dataclass
class LoggingConfig:
    log_level: str
    log_format: str


@dataclass
class Config:
    app: AppConfig
    bot: BotConfig
    chat_gpt: ChatGptConfig
    sqlite: SqliteConfig
    logging: LoggingConfig


def load_from_dotenv_file():
    found_dotenv_path = find_dotenv()
    load_dotenv(found_dotenv_path)


def get_config() -> 'Config':
    load_from_dotenv_file()

    env = os.environ

    bled_chat_id = env['BLED_CHAT_ID']
    bot_token = env['BOT_TOKEN']
    openai_model = env['OPENAPI_MODEL']
    openai_token = env['OPENAI_API_KEY']
    openai_chat_context = env['OPENAI_CHAT_CONTEXT']
    sqlite_db_filepath = Path(env['SQLITE_DATABASE_FILEPATH'])
    sqlite_db_filename = Path(env['SQLITE_DATABASE_FILENAME'])
    logging_log_level = env['LOGGING_LOG_LEVEL']
    logging_log_format = env['LOGGING_FORMAT']

    return Config(
        app=AppConfig(
            bled_chat_id=bled_chat_id
        ),
        bot=BotConfig(
            token=bot_token
        ),
        chat_gpt=ChatGptConfig(
            model=openai_model,
            token=openai_token,
            chat_context=openai_chat_context
        ),
        sqlite=SqliteConfig(
            filepath=sqlite_db_filepath,
            filename=sqlite_db_filename
        ),
        logging=LoggingConfig(
            log_level=logging_log_level,
            log_format=logging_log_format
        )
    )
