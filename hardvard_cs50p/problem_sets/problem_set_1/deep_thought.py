def main() -> None:
  user_input = input("What is The Answer to the Great Question?: ")
  if isFortyTwo(user_input):
    print("Yes")
  else:
    print("No")

def isFortyTwo(string: str) -> bool:
  match string.lower():
    case "42":
      return True
    case "forty-two":
      return True
    case "forty two":
      return True
    case _:
      return False

if __name__ == '__main__':
  main()