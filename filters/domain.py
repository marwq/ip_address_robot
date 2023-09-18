from aiogram.filters import Filter
from aiogram.types import Message

from tld import domains


class Domain(Filter):
    async def __call__(self, message: Message) -> bool:
        parts = message.text.split('.')
        if len(parts) == 1:
            return False

        if not (parts[-1] in domains):
            return False
            
        return True