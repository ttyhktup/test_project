from lib.greet import *

def test_greet_returns_hello_john():
    result = greet("John")
    assert result == "Hello, John!"