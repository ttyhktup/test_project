from lib.report_length import *

def test_report_length_five():
    result = report_length("ouch!")
    assert result == f"This string was 5 characters long."

def test_report_length_eleven():
    result = report_length("abracadabra")
    assert result == f"This string was 11 characters long."