from aiogram import Router
from aiogram.types import (
    Message, InlineKeyboardMarkup, 
    InlineKeyboardButton, WebAppInfo
)
from ipinfo import getHandlerAsync

import config
from filters import IpAddress, Domain
from tools import remove_proto, getaddrbyhostname
from .loader import loader


handler = getHandlerAsync(config.IPINFO_TOKEN)
router = Router()


@router.message(IpAddress())
@loader
async def _(m: Message):
    ip_addr = remove_proto(m.text)
    result = await handler.getBatchDetails([ip_addr])
    data: dict = result[ip_addr]
    
    map_url = f'https://www.google.com/maps?q={data["latitude"]},{data["longitude"]}'
    
    return dict(
        text=f'🌐 IP Address {ip_addr}\n\n'
        f'{data["country_flag"]["emoji"]}<code>{data.get("country_name", "Not found")}</code>'
        f'<code>, {data.get("city", "Not found")}</code>\n'
        f'Hostname: <code>{data.get("hostname", "Not found")}</code>\n'
        f'Organization: <code>{data.get("org", "Not found")}</code>\n'
        f'Postal Code: <code>{data.get("postal", "Not found")}</code>\n\n'
        f'Location: <a href="{map_url}">[Google maps]</a>',
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='Torrent downloads', 
                    web_app=WebAppInfo(url=f'https://iknowwhatyoudownload.com/en/peer/?ip={ip_addr}'))
            ]
        ])
    )
    

@router.message(Domain())
@loader
async def _(m: Message):
    domain = remove_proto(m.text)
    ip_addr = await getaddrbyhostname(domain)
    result = await handler.getBatchDetails([ip_addr])
    data: dict = result[ip_addr]
    
    map_url = f'https://www.google.com/maps?q={data["latitude"]},{data["longitude"]}'
    
    return dict(
        text=f'🌐 Domain {domain}\n\n'
        f'{data["country_flag"]["emoji"]}<code>{data.get("country_name", "Not found")}</code>'
        f'<code>, {data.get("city", "Not found")}</code>\n'
        f'Hostname: <code>{data.get("hostname", "Not found")}</code>\n'
        f'IP: <code>{ip_addr}</code>\n'
        f'Organization: <code>{data.get("org", "Not found")}</code>\n'
        f'Postal Code: <code>{data.get("postal", "Not found")}</code>\n\n'
        f'Location: <a href="{map_url}">[Google maps]</a>',
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='Torrent downloads', 
                    web_app=WebAppInfo(url=f'https://iknowwhatyoudownload.com/en/peer/?ip={ip_addr}'))
            ]
        ])
    )