def main() -> None:
  dollars = dollars_to_float(input("how much was the meal?: "))
  percent = percent_to_float(input("what percentage would you like to tip?: "))
  tip = dollars * percent
  print("tip amount: ", f"${tip:.2f}")

def dollars_to_float(dollars: str) -> float:
  return float(dollars[1:])

def percent_to_float(percent: str) -> float:
  return float(percent[:-1]) / 100


if __name__ == '__main__':
  main()