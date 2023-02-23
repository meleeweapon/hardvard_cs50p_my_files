def main() -> None:
  # first_number = input("first number: ")
  # operator = input("operator: ")
  # second_number = input("second number: ")
  first_number, operator, second_number = interpret(input())
  print(execute(first_number, operator, second_number))

def execute(first_number: str, operator: str, second_number: str) -> str:
  result = 0.0
  match operator:
    case "+":
      result = int(first_number) + int(second_number)
    case "-":
      result = int(first_number) - int(second_number)
    case "*":
      result = int(first_number) * int(second_number)
    case "/":
      result = int(first_number) / int(second_number)
  
  return f"{result:.1f}"


def interpret(input: str) -> list[str]:
  return input.split(" ")

if __name__ == '__main__':
  main()