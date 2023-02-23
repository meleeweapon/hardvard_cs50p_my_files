import random

def main() -> None:
  print("enter level")
  level = force_get_positive_int()

  secret = random.randint(1, level)

  print(f"guess the number between 1 and {level}")
  while True:
    guess = force_get_positive_int()
    if guess < secret:
      print("too small")
    elif guess > secret:
      print("too large")
    else:
      print("you guessed correct")
      break

def force_get_positive_int() -> int:
  while True:
    user_input = input("enter a positive integer: ")
    try:
      level = int(user_input)
    except ValueError:
      continue
    if level <= 0:
      continue
    return level


if __name__ == '__main__':
  main()