from lib.check_codeword import *

def test_check_codeword_if_horse():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_check_codeword_if_similar():
    result = check_codeword("home")
    assert result == "Close, but nope."

def test_check_codeword_if_wrong():
    result = check_codeword("condo")
    assert result == "WRONG!"