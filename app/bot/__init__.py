from typing import TYPE_CHECKING

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from pydantic import SecretStr

from app.bot import handlers

if TYPE_CHECKING:
    from app.libs.wiki_api import WikiAPI
    from app.libs.chatgpt import ChatGptAPI


async def start(
        bot_token: SecretStr,
        wiki_api_instance: 'WikiAPI',
        chat_gpt_instance: 'ChatGptAPI'
) -> None:
    bot = Bot(
        token=bot_token.get_secret_value(),
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML,
            link_preview_is_disabled=True
        )
    )

    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(handlers.root_router)

    dp['wiki_api'] = wiki_api_instance
    dp['chat_gpt'] = chat_gpt_instance

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
