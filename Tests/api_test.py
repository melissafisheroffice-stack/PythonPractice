import requests

BASE_URL = "https://restful-booker.herokuapp.com"

def test_get_booking_ids():
    response = requests.get(f"{BASE_URL}/booking")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    print(f"Found {len(response.json())} bookings")
    return response.json()