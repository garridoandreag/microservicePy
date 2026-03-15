from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_get_accounts_returns_all_accounts() -> None:
    response = client.get("/accounts")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 3
    assert data[0]["accountNumber"] == "1001"


def test_get_account_by_number_returns_account() -> None:
    response = client.get("/accounts/1002")

    assert response.status_code == 200
    data = response.json()
    assert data["accountNumber"] == "1002"
    assert data["firstName"] == "Carlos"
    assert data["lastName"] == "Ramirez"


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
