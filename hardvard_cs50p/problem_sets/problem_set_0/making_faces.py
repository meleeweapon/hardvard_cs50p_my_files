def main() -> None:
  user_input = input("smile or frown: ")
  print("output:", convert(user_input))

def convert(string: str) -> str:
  result = string
  result = result.replace(":)", "🙂")
  result = result.replace(":(", "🙁")
  return result

if __name__ == '__main__':
  main()