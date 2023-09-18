import pytest

from aiogram.types import Message

from filters import Domain, IpAddress


def get_message(**kwargs):
    return Message(
        message_id=1,
        date=1,
        chat={
            'type': '1',
            'id': 1
        },
        **kwargs
    )


class TestIpAddress:
    filter = IpAddress()
    
    async def check(text: str) -> bool:
        return await TestIpAddress.filter(get_message(text=text))
    
    @pytest.mark.asyncio
    async def test_one(self):
        assert await TestIpAddress.check('127.0.0.1') == True
    
    @pytest.mark.asyncio
    async def test_two(self):
        assert await TestIpAddress.check('127.0.256.1') == False
        
    @pytest.mark.asyncio
    async def test_three(self):
        assert await TestIpAddress.check('127.0.127') == False
        
    @pytest.mark.asyncio
    async def test_four(self):
        assert await TestIpAddress.check('127.0.abc.125') == False
        

class TestDomain:
    filter = Domain()
    
    async def check(text: str) -> bool:
        return await TestDomain.filter(get_message(text=text))
    
    @pytest.mark.asyncio
    async def test_one(self):
        assert await TestDomain.check('domain.com') == True
        
    @pytest.mark.asyncio
    async def test_two(self):
        assert await TestDomain.check('domain') == False
        
    @pytest.mark.asyncio
    async def test_three(self):
        assert await TestDomain.check('www.domain.kz') == True
        
    @pytest.mark.asyncio
    async def test_four(self):
        assert await TestDomain.check('domain.some') == False