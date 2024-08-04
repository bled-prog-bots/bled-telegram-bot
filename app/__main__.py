import asyncio

from app import bot, logger_config
from app.config import settings
from app.libs.chatgpt import ChatGptAPI
from app.libs.wiki_api import WikiAPI


async def main():
    logger_config.setup(settings.ENVIRONMENT)

    wiki_api = WikiAPI()
    chat_gpt = ChatGptAPI(
        settings.OPENAPI_MODEL,
        settings.OPENAI_API_KEY,
        settings.OPENAI_CHAT_CONTEXT
    )

    await bot.start(
        settings.BOT_TOKEN,
        wiki_api,
        chat_gpt
    )


if __name__ == '__main__':
    asyncio.run(main())
