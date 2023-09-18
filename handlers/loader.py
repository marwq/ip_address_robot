import asyncio
import inspect

from typing import Coroutine

from aiogram.types import Message


def loader(handler: Coroutine):
    async def wrapper(m: Message, **kwargs):
        required_keys = inspect.signature(handler).parameters.keys()
        required_kwargs = dict(
            filter(
                lambda it: it[0] in required_keys, 
                kwargs.items()
            )
        )
        task = asyncio.create_task(
            handler(m, **required_kwargs)
        )
        sent_msg = await m.answer('⏳ Wait...')
        await task
        result: dict = task.result()
        await sent_msg.edit_text(**result)
    
    return wrapper