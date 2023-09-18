import asyncio
import csv


with open('top-level-domain-names.csv', 'r', encoding='utf8') as csvfile:
    csvreader = csv.DictReader(csvfile)
    domains = {
        row['Domain']: (row['Type'], row['Sponsoring Organisation'])
        for row in csvreader
    }


def remove_proto(url: str) -> str:
    return url.removeprefix('https://') \
              .removeprefix('http://') \
              .strip('/')
              

async def getaddrbyhostname(hostname: str) -> str:
    loop = asyncio.get_running_loop()
    _, _, _, _, (addr, _) = (await loop.getaddrinfo(hostname, 80))[0]
    return addr