import re

def main() -> None:
  test_cases = ["127.0.0.1", "255.255.255.255", "0.0.0.0", "512.512.512.512", "1.2.3.1000", "cat"]
  for case in test_cases:
    print(f"{case} is {valid_ipv4_adress(case)}")

def valid_ipv4_adress(adress: str) -> bool:
  if matches := re.match(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", adress):
    parts = matches.groups()
    if len(parts) != 4:
      return False
    for part in parts:
      try:
        part_int = int(part)
      except ValueError:
        return False
      if part_int < 0 or part_int > 255:
        return False
    return True
  return False

# def valid_ipv4_adress(adress: str) -> bool:
#   return bool(re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", adress))


if __name__ == '__main__':
  main()