from aiogram import Router

from . import chat
from app.bot.filters import IsBledChatFilter

root_router = Router(name='root router')
root_router.message.filter(
    IsBledChatFilter()
)
root_router.include_routers(
    chat.chat_router
)
