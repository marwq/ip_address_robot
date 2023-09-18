from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message


router = Router()


@router.message(CommandStart())
async def _(m: Message):
    await m.answer(
        '''🇬🇧
Functions: 
- Enter IP address or domain. Example:
<code>140.82.121.4</code> or <code>github.com</code>

🇷🇺
Функции:
- Введите IP-адрес или домен. Пример:
<code>140.82.121.4</code> или <code>github.com</code>
        '''
    )