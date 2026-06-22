import requests

BASE_URL = "https://restful-booker.herokuapp.com"

def test_get_booking_ids():
    response = requests.get(f"{BASE_URL}/booking")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    print(f"Found {len(response.json())} bookings")
    return response.json()

def test_health_check():
    response = requests.get(f"{BASE_URL}/ping")
    assert response.status_code == 201
    assert response.text == "Created"

# Test identified that the status code is incorrect - 201 instead of 200

def test_auth_token():
    response = requests.post(f"{BASE_URL}/auth", json={"username": "admin", "password": "password123"})
    assert response.status_code == 200
    return response.json()
# changed the status code to 400 and fails as expected
