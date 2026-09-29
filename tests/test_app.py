import pytest
from app import create_app


@pytest.fixture
def client():
    return create_app().test_client()


def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert res.get_json()["status"] == "ok"

def test_create_and_get_item(client):
    res = client.post("/items", json={"name": "book"})
    assert res.status_code == 201
    item_id = res.get_json()["id"]
    assert client.get(f"/items/{item_id}").get_json()["name"] == "book"


def test_create_requires_name(client):
    assert client.post("/items", json={}).status_code == 400


def test_delete_item(client):
    item_id = client.post("/items", json={"name": "pen"}).get_json()["id"]
    assert client.delete(f"/items/{item_id}").status_code == 204
    assert client.get(f"/items/{item_id}").status_code == 404