import re

def main() -> None:
  test_cases = ["boobaAwooga", "name", "firstName", "prefferedFirstName"]
  for case in test_cases:
    print("camel case: " + case)
    print("snake case: " + camel_case_to_snake_case(case))

def camel_case_to_snake_case(string: str) -> str:
  """
  returns a string reformatted to snake-case from camel-case
  """

  result = string
  # handle underscores
  offset = 0 # everytime underscore is inserted index shifts by one,
  # offset is to compensate for that
  for index, char in enumerate(string):
    if char.isupper():
      result = result[:index + offset] + "_" + result[index + offset:]
      offset += 1
  if result[0] == "_":
    result = result[1:]
  
  # handle uppercase
  result = result.lower()

  return result


if __name__ == '__main__':
  main()