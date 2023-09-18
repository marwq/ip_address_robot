import sys
import asyncio
import logging

from aiogram import Bot, Dispatcher

import config
from handlers import register_routers


async def main():
    bot = Bot(token=config.BOT_TOKEN, parse_mode='HTML')
    await bot.delete_my_commands()
    await bot.delete_webhook()
    
    dp = Dispatcher()
    register_routers(dp)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())