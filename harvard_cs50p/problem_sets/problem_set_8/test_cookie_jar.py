import pytest
from cookie_jar import *

def test_init():
  with pytest.raises(ValueError):
    CookieJar(-1)
    CookieJar(-2)
    CookieJar(-3)
    CookieJar(2, cookies=3)
    CookieJar(2, cookies=-3)

def test_str():
  jar = CookieJar(3)
  assert str(jar) == ""
  jar.deposit(1)
  assert str(jar) == "🍪"
  jar.deposit(2)
  assert str(jar) == "🍪🍪🍪"

def test_deposit():
  with pytest.raises(ValueError):
    CookieJar(4).deposit(5)
    CookieJar(0).deposit(1)
    CookieJar(5, cookies=5).deposit(-3)
    CookieJar(3).deposit("cat")
    CookieJar(3).deposit("1")


def test_withdraw():
  with pytest.raises(ValueError):
    CookieJar(3).deposit(1)
    CookieJar(3).deposit(-1)
    CookieJar(3, cookies=3).deposit(4)
    CookieJar(3).deposit("dog")
    CookieJar(3).deposit("1")