def main() -> None:
  user_input = input("say something: ")
  print(omit_vowels(user_input))

  test_cases = ["Twitter", "What's your name?", "CS50"]
  for case in test_cases:
    print(case)
    print(omit_vowels(case))

def is_lower_case_vowel(char: str) -> bool:
  """
  returns true if the given character is a lower-case vowel
  """
  match char:
    case "a" | "e" | "i" | "o" | "u":
      return True
    case _:
      return False


def omit_vowels(string: str) -> str:
  """
  returns a copy of the string without any vowels in it
  """
  return "".join(char for char in string if not is_lower_case_vowel(char.lower()))
  return "".join(filter(lambda char: not is_lower_case_vowel(char.lower()), string))

if __name__ == '__main__':
  main()