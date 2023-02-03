import pytest
from hello import hello

def test_hello_str():
  assert hello("world") == "hello world"

def test_hello_default():
  assert hello() == "hello "