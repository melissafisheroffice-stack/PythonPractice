# session is kept for the entire test run

import pytest

@pytest.fixture(scope="session")
def database():
    print("Connecting to database")
    return "Connected"

def test_database(database):
    print(database)
    assert database == "Connected"