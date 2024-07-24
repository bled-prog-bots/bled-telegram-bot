from aiogram import Router
from aiogram.filters.command import Command
from aiogram.types import Message

router = Router(name='ping command router')


@router.message(Command(commands=['bled_ping']))
async def ping(msg: Message):
    await msg.reply('PONG')
