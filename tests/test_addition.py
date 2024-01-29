# File: tests/test_add_five.py
from lib.addition import *

def test_add_five_returns_eight_for_three():
    result = add_five(3)
    assert result == 8
