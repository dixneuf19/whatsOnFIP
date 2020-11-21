import pytest
from fastapi.encoders import jsonable_encoder

from whatsonfip.unofficial_api import get_now_unofficial
from whatsonfip.models import Song


@pytest.mark.asyncio
async def test_get_now_unofficial():
    assert Song(**get_now_unofficial().dict())
