def main() -> None:
  user_input = input("greeting: ")
  print(f"you owe ${bank_greeting_procedure(user_input)}")

def bank_greeting_procedure(greeting: str) -> int:
  greeting = greeting.lower()
  if greeting[:5] == "hello":
    return 0
  elif greeting[0] == "h":
    return 20
  else:
    return 100

if __name__ == '__main__':
  main()