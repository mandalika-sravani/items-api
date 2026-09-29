import pytest
from app import create_app


@pytest.fixture
def client():
    return create_app().test_client()


def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert res.get_json()["status"] == "ok"