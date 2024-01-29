import pytest
from lib.present import *

def test_present():
    present = Present()
    present.wrap("names")
    result = present.unwrap()
    assert result == "names"