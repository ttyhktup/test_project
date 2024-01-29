from lib.gratitudes import *

def test_gratitudes():
    gratitudes = Gratitudes()
    gratitudes.add("help")
    gratitudes.add("support")
    gratitudes.add("luck")
    result = gratitudes.format()
    assert result == "Be grateful for: help, support, luck"