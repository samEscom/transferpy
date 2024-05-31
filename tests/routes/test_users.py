from tests.routes.client import client
from tests.routes.constants import UserTest


def test_fail_login(client):
    response = client.post(
        "user/login", json={"email": "fail@fail.com", "password": "1234"}
    )

    assert response.status_code == 200
    assert response.json.get("data") == "error on user or password"


def test_user_register_and_good_login(client):
    response = client.post(
        "user/register",
        json={
            "name": UserTest.name,
            "email": UserTest.email,
            "password": UserTest.password,
            "fullname": UserTest.fullname,
            "address": UserTest.address,
            "phone_number": UserTest.phone_number,
        },
    )

    assert response.status_code == 200

    assert isinstance(response.json.get("data").get("id"), int)
    assert response.json.get("data").get("name") == UserTest.name
    assert response.json.get("data").get("email") == UserTest.email
    assert response.json.get("data").get("phoneNumber") == UserTest.phone_number

    response = client.post(
        "user/login",
        json={
            "email": UserTest.email,
            "password": UserTest.password,
        },
    )

    assert response.status_code == 200
    assert isinstance(response.json.get("data").get("token"), str)
