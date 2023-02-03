# if a folder has __init__.py in it, it is considered to be a package,
# pytest can test whole folders if they are packages
# try in console to run pytest on test_hello directory
from hello import hello

def test_hello_default():
  assert hello() == "hello "

def test_hello_argument():
  assert hello("awooga") == "hello awooga"

