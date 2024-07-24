from aiogram import Router

from . import wiki, ping, chat_gpt

chat_router = Router(name='chat router')
chat_router.include_routers(
    wiki.router,
    ping.router,
    chat_gpt.router
)
