from aiogram.filters import Filter
from aiogram.types import Message

from tools import remove_proto


class IpAddress(Filter):
    async def __call__(self, m: Message) -> bool:
        text = remove_proto(m.text)
        parts = text.split('.')
        if len(parts) != 4:
            return False

        for part in parts:
            if not (part.isnumeric() and int(part) in range(0, 256)):
                return False
            
        return True