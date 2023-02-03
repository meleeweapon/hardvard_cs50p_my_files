def main() -> None:
  print(fuel_gauge())

def ratio_to_percentage(x: int, y: int) -> int:
  """
  returns a rounded percentage value equivalent to x/y
  expects x and y to be ints
  """
  return round((x * 100) / y)

def fuel_gauge() -> str:
  while True:
    user_input = input("enter a ratio of ints as x/y: ")
    x, y = user_input.split("/")

    # convert x and y to int
    try:
      x = int(x)
      y = int(y)
    except ValueError:
      print("x and y must be integers")
      continue

    try:
      percentage = ratio_to_percentage(x, y)
    except ZeroDivisionError:
      print("y mustn't be 0")
      continue

    if x > y:
      print("x mustn't be greater than y")
      continue

    final_string = f"{percentage}%"
    if percentage <= 1:
      final_string = "E"
    elif percentage >= 99:
      final_string = "F"
    
    return final_string



if __name__ == '__main__':
  main()