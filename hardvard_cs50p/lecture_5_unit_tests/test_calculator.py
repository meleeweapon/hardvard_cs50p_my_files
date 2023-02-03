# from calculator import square

# def main():
#   test_square()

# def test_square():
#   # if square(2) != 4:
#   #   print("squared(2) was not 4")
#   # if square(3) != 9:
#   #   print("squared(3) was not 9")

#   # assert square(2) != 4
#   # assert square(3) != 9


#   try:
#     assert square(2) == 4
#   except AssertionError:
#     print("square(2) was not 4")
  
#   try:
#     assert square(3) == 9
#   except AssertionError:
#     print("square(3) was not 9")

#   try:
#     assert square(-2) == 4
#   except AssertionError:
#     print("square(-2) was not 4")

#   try:
#     assert square(-3) == 9
#   except AssertionError:
#     print("square(-3) was not 9")

#   try:
#     assert square(0) == 0
#   except AssertionError:
#     print("square(0) was not 0")







# if __name__ == "__main__":
#   main()




# # pytest test_calculator.py
# from calculator import square

# def test_square():
#   assert square(2) == 4
#   assert square(3) == 9
#   assert square(-2) == 4
#   assert square(-3) == 9
#   assert square(0) == 0




# pytest test_calculator.py
from calculator import square
import pytest

def test_square_positive():
  assert square(2) == 4
  assert square(3) == 9

def test_square_negative():
  assert square(-2) == 4
  assert square(-3) == 9

def test_square_zero():
  assert square(0) == 0

def test_square_string():
  with pytest.raises(TypeError):
    square("cat")