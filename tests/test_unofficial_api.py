import pytest

from whatsonfip.unofficial_api import get_now_unofficial
from whatsonfip.models import Track


@pytest.mark.asyncio
async def test_get_now_unofficial():
    assert Track(**get_now_unofficial().dict())
