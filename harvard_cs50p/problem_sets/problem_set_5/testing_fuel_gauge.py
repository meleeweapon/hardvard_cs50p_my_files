def main() -> None:
  print(gauge(convert(input("enter gauge: "))))


def convert(ratio: str) -> int:
  x_and_y = ratio.split("/")
  if len(x_and_y) != 2:
    print("ratio must be formatted as x/y")
    raise ValueError
  
  x, y = x_and_y
  x = x.strip()
  y = y.strip()

  try:
    x = int(x)
    y = int(y)
  except ValueError:
    raise ValueError
  
  if y == 0:
    print("y must not be 0")
    raise ZeroDivisionError

  if x > y:
    print("x mustn't be greater than y")
    raise ValueError

  return round((x * 100) / y)


def gauge(percentage: int) -> str:
  if percentage <= 1:
    final_string = "E"
  elif percentage >= 99:
    final_string = "F"
  else:
    final_string = f"{percentage}%"
    
  return final_string



if __name__ == '__main__':
  main()