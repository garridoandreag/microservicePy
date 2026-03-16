from fastapi.testclient import TestClient

from main import app


client = TestClient(app)



def test_get_account_by_number_not_found() -> None:
    response = client.get("/accounts/9999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Account not found"}


def test_health_check() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "OK", "version": "v1"}


def test_version_check() -> None:
    response = client.get("/version")

    assert response.status_code == 200
    assert response.json() == {"version": "v1"}
