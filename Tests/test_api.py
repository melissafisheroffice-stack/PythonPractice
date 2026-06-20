"""
Come back to this api testing later
"""

import requests

def test_duckduckgo_instant_answer(api):

    # Arrange
    url = "https://duckduckgo.com/?qpython+programming&format=json"

    # Act
    response = requests.get(url)
    body=response.json()

    # Assert
    assert response.status_code == 200
    assert 'Python' in body['AbstractText']
