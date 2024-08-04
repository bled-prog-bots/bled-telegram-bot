from typing import Literal

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    ENVIRONMENT: Literal['dev', 'prod']
    BLED_CHAT_ID: int
    BOT_TOKEN: SecretStr
    OPENAPI_MODEL: str
    OPENAI_API_KEY: SecretStr
    OPENAI_CHAT_CONTEXT: str

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()
