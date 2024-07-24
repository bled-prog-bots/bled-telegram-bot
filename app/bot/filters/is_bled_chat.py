from aiogram.types import Message
from aiogram.filters import BaseFilter


class IsBledChatFilter(BaseFilter):
    def __init__(self):
        ...

    async def __call__(self, message: Message) -> bool:
        # TODO: Сделать нормально
        return message.chat.id == -1001309576488
