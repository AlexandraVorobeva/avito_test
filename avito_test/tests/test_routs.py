from fastapi.testclient import TestClient
from ..app.main import app

client = TestClient(app)


def test_get_operations():
    response = client.get("/operations/")
    assert response.status_code == 200


def test_get_operation():
    response = client.get("/operations/5/")
    assert response.status_code == 200


def test_get_client():
    response = client.get("/clients/1/")
    assert response.status_code == 200


def test_post_client():
    response = client.post("/clients/", json={
        "first_name": "Sasha",
        "last_name": "Vorobeva",
        "balance": 0
    })
    assert response.status_code == 200


def test_get_operations_for_client():
    response = client.get("/clients/all_operations/1/")
    assert response.status_code == 200


def test_get_operations_per_day():
    response = client.get("/clients/operations_per_day/1/2021-12-23/")
    assert response.status_code == 200
