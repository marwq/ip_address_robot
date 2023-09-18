from aiogram.filters import Filter
from aiogram.types import Message

from tools import remove_proto, domains


class Domain(Filter):
    async def __call__(self, m: Message) -> bool:
        text = remove_proto(m.text)
        parts = text.split('.')
        if len(parts) == 1:
            return False

        if not (parts[-1] in domains):
            return False
            
        return True