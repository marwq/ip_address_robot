import logging

from aiogram import Router, F, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import CHAT_ID


router = Router()


@router.message(CommandStart())
async def _(m: Message, bot: Bot):
    await m.answer(
        '🇬🇧\nFunctions:\n'
        '- Enter IP address or domain. Example:\n'
        '<code>140.82.121.4</code> or <code>github.com</code>\n\n'
        '🇷🇺\nФункции:\n'
        '- Введите IP-адрес или домен. Пример:\n'
        '<code>140.82.121.4</code> или <code>github.com</code>'
    )
    
    # Sorry for some piece of govnocode. Temporary solution
    user = f'{m.from_user.first_name} {m.from_user.last_name} {m.from_user.username} {m.from_user.id}'
    logging.info(user)
    await bot.send_message(CHAT_ID, user)