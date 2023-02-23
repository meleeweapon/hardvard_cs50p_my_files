import string
import re

def main() -> None:
  # plate = input("Plate: ")
  test_cases = ["CS50", "CS05", "CS50P", "PI3.14", "H", "OUTATIME",]
  for case in test_cases:
    if valid_vanity_plate(case):
        print(f"{case} Valid")
    else:
        print(f"{case} Invalid")
  # valid_vanity_plate("AAA22A")



def valid_vanity_plate(plate: str) -> bool:
  """
  plate must be only upper-case characters
  returns true if the given plate is valid
  """
  # “All vanity plates must start with at least two letters.”
  # “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
  # “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
  # “No periods, spaces, or punctuation marks are allowed.”
  
  # check if at least 2 at most 6 chars
  if not (len(plate) >= 2 and len(plate) <= 6):
    return False
  # max 6 chars (letter or num) min 2 chars
  # check if all chars are letter or num
  for char in plate:
    if not (char.isalpha() or char.isnumeric()):
      return False

  # must start with at least two letters 
  # do this after min 2 chars check or program will crash
  if not (plate[0].isalpha() and plate[1].isalpha()):
    return False
  
  # nums must come at the end, not in the middle or beginning
  # first num cant be a 0
  nums_started = False
  for char in plate:
    if nums_started:
      if not char.isnumeric():
        return False
    else:
      # this should get executed only once,
      # when this gets executed it's the first num
      if char.isnumeric():
        if char == "0":
          return False
        nums_started = True

  # no periods, spaces or punctuation marks
  if " " in plate:
    return False
  if "." in plate:
    return False
  for char in plate:
    if char in string.punctuation:
      return False
  
  # if all checks pass, return true
  return True


def valid_vanity_plate(plate: str) -> bool:
  if not (len(plate) >= 2 and len(plate) <= 6):
    return False
  if not plate.isalnum():
    return False
  if not plate[:2].isalpha():
    return False
  
  # find the first nums ind
  first_num_ind = None
  for ind, char in enumerate(plate):
    if char.isdigit():
      first_num_ind = ind
      break
  # if a num is found, slice the number part and check if
  # it's all digits
  if first_num_ind is not None:
    if plate[first_num_ind] == "0":
      return False
    number_part = plate[first_num_ind:]
    if not number_part.isdigit():
      return False
  
  for char in plate:
    if char.isspace() or char in string.punctuation:
      return False
  
  return True


def valid_vanity_plate(plate: str) -> bool:
  if not (len(plate) >= 2 and len(plate) <= 6):
    return False
  if not plate.isalnum():
    return False
  if not plate[:2].isalpha():
    return False
  
  for char in plate:
    if char.isdigit():
      first_num = char
      if first_num == "0":
        return False
      _, number_part = plate.split(first_num, 1)
      if not number_part.isdigit():
        return False
      break
  
  if " " in plate:
    return False

  return True


def valid_vanity_plate(plate: str) -> bool:
  return (len(plate) >= 2 and len(plate) <= 6) and (re.match(r"^[a-zA-Z]{2}[a-zA-Z]*[1-9][0-9]*$", plate))


if __name__ == '__main__':
  main()