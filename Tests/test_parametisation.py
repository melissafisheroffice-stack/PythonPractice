"""
Instead of writing the same test multiple times with different inputs, parameterization lets you write the test once and provide multiple sets of data.
"""


import pytest

@pytest.mark.parametrize("test_input,expected", [("3+7", 10), ("200*10",2000)])
def test_evals(test_input, expected):
    assert eval(test_input) == expected
