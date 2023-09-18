from aiogram.filters import Filter
from aiogram.types import Message


class IpAddress(Filter):
    async def __call__(self, message: Message) -> bool:
        parts = message.text.split('.')
        if len(parts) != 4:
            return False

        for part in parts:
            if not (part.isnumeric() and int(part) in range(0, 256)):
                return False
            
        return True