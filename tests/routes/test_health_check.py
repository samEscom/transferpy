from tests.routes.client import client


def test_health_check(client):
    response = client.get("health-check")

    assert response.status_code == 200
    assert response.json.get("data").get("status") == "OK"
