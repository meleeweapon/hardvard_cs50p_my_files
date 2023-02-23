from testing_vanity_plates import *

def test_valid_vanity_plate():
  assert valid_vanity_plate("CS50") == True
  assert valid_vanity_plate("CS05") == False
  assert valid_vanity_plate("CS50P") == False
  assert valid_vanity_plate("PI3.14") == False
  assert valid_vanity_plate("H") == False
  assert valid_vanity_plate("OUTATIME") == False