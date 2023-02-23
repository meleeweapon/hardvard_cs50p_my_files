def main() -> None:
  # number = int(input("what's x? "))
  number = input("what's x? ")
  print("x squared is", square(number))

def square(number):
  return number * number
  # return number + number



if __name__ == "__main__":
  main()