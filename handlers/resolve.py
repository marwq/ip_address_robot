import asyncio

from aiogram import Router
from aiogram.types import Message

from filters import IpAddress, Domain


router = Router()


@router.message(IpAddress())
async def _(m: Message):
    await m.answer('IP detected')
    

@router.message(Domain())
async def _(m: Message):
    loop = asyncio.get_running_loop()
    _, _, _, _, (addr, _) = (await loop.getaddrinfo(m.text, 80))[0]
    await m.answer(f'Domain detected: {addr}', parse_mode=None)