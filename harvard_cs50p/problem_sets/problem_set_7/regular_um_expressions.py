import re

def count(string: str) -> int:
  if matches := re.findall(r"(?:\bum\b)", string.lower()):
    return len(matches)
  else:
    return 0

def main():
  print(count("um")) # 1
  print(count("um?")) # 1
  print(count("Um, thank for the album.")) # 1
  print(count("Um, thanks, um...")) # 2
  print(count("yeah um uhh")) # 1
  print(count("hello um, world")) # 1


if __name__ == '__main__':
  main()