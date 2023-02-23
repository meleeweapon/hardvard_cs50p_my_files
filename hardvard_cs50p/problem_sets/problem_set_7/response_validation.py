from validators import email

def main() -> None:
  test_cases = [
    ("malan@harvard.edu", True),
    ("mstar19077@hotmail.com", True),
    ("malan@@@harvard.edu", False),
    ("mstar19077@hotmail..com", False),
  ]
  for case, expected_result in test_cases:
    result = valid_email(case)
    if result != expected_result:
      print("failed", case, result)
    else:
      print("success", case, result)

def valid_email(email_adress: str) -> bool:
  if email(email_adress) == True:
    return True
  else:
    return False


if __name__ == '__main__':
  main()