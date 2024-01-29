from lib.string_builder import *

def test_string_builder_output():
    string_builder = StringBuilder()
    string_builder.add("Hello")
    # string_builder.size()
    result = string_builder.output()
    assert result == "Hello"

def test_string_builder_str_len():
    string_builder = StringBuilder()
    string_builder.add("Hello")
    result = string_builder.size()
    assert result == 5