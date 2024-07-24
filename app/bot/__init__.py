import typing

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from app.bot import handlers
from app.lib.wiki_api import WikiAPI
from app.lib.chatpt import ChatGptAPI

if typing.TYPE_CHECKING:
    from app.config import Config


async def start(config: 'Config') -> None:
    bot = Bot(
        token=config.bot.token,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML,
            link_preview_is_disabled=True
        )
    )

    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(handlers.root_router)

    dp['wiki_api'] = WikiAPI()
    dp['chat_gpt'] = ChatGptAPI(
        config.chat_gpt.model,
        config.chat_gpt.token,
        config.chat_gpt.chat_context
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
