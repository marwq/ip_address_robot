from aiogram import Dispatcher

from .menu import router as menu
from .resolve import router as resolve


def register_routers(dp: Dispatcher):
    dp.include_routers(
        menu,
        resolve,
    )