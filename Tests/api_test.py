import requests
import pytest

BASE_URL = "https://restful-booker.herokuapp.com"

def test_create_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(
        f"{BASE_URL}/auth",
        json=payload,
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 200
    body = response.json()
    assert "token" in body
    assert isinstance(body["token"], str)
    print(f"\nToken: {body['token']}")

@pytest.fixture(scope="session")
def auth_headers(auth_token):
    return {
        "Content-Type": "application/json",
        "Cookie": f"token={auth_token}"
    }
#fixture is a reusable setup.  This  auth token could be reused in a later test.  Logins are another common one.
def test_get_booking_ids():
    response = requests.get(f"{BASE_URL}/booking")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_health_check():
    response = requests.get(f"{BASE_URL}/ping")
    assert response.status_code == 201
    assert response.text == "Created"

# Test identified that the status code is incorrect - 201 instead of 200

def test_auth_token():
    response = requests.post(f"{BASE_URL}/auth", json={"username": "admin", "password": "password123"})
    assert response.status_code == 200
# changed the status code to 400 and fails as expected
