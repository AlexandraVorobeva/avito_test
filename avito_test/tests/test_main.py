from fastapi.testclient import TestClient
from avito_test.app.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("http://localhost:8005/operations/?kind=income")

    assert response.status_code == 200
