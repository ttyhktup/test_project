from lib.password_checker import *

def test_password_checker():
    password_checker = PasswordChecker()
    result = password_checker.check("dwede")
    assert result == True