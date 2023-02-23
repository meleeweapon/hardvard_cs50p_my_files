from testing_fuel_gauge import *
import pytest

def test_convert():
  assert convert("3/4") == 75
  assert convert("3/6") == 50
  assert convert("10/10") == 100
  assert convert("0/3") == 0
  assert convert(" 3 / 4 ") == 75

def test_exceptions__convert():
  with pytest.raises(ValueError):
    convert("")
    convert("3/4/5")

    convert("abc/4")
    convert("3/abc")
    convert("/")
    convert("3/")
    convert("/4")
    convert("1.7/4")

    convert("5/4")
  
  with pytest.raises(ZeroDivisionError):
    convert("3/0")


def test_gauge():
  assert gauge(0) == "E"
  assert gauge(100) == "F"
  assert gauge(50) == "50%"