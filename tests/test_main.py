from fastapi.testclient import TestClient

from whatsonfip.main import app
from whatsonfip.models import Song, Station

client = TestClient(app)


def test_get_live():
    response = client.get("/live")
    assert response.status_code in (200, 204)
    if response.status_code == 200:
        assert Song(**response.json())


def test_get_stations():
    response = client.get("/stations")
    assert response.status_code == 200
    assert [Station(**s) for s in response.json()]


def test_get_health():
    response = client.get("/health")
    assert response.status_code == 200


def test_get_api_status():
    response = client.get("/api-status")
    assert response.status_code == 200
    assert response.json()["code"] in (200, 500)
