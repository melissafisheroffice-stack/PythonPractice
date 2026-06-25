import pytest
# @mark Labels tests, skip tests, mark expected failures, categorize tests

@pytest.mark.smoke
def test_multiplication():
    assert 5*10 ==50

@pytest.mark.smoke
def test_division():
    assert 10 / 2 ==5

