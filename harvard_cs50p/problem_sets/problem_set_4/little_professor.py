import random

def main() -> None:
  level = get_level()

  score = 0
  for _ in range(10):
    x = generate_integer(level)
    y = generate_integer(level)
    answered_correctly = False
    for _ in range(3):
      answer = input(f"{x} + {y} = ")
      try:
        answer = int(answer)
      except ValueError:
        print("EEE")
        continue
      if answer != x + y:
        print("EEE")
      else:
        answered_correctly = True
        score += 1
        break
    if not answered_correctly:
      print(x + y)
  
  print("your score is " + str(score))


def get_level() -> str:
  while True:
    result = force_get_int("enter level: ")
    match result:
      case 1|2|3:
        return result
      case _:
        continue

def force_get_int(prompt="") -> int:
  while True:
    user_input = input(prompt)
    try:
      result = int(user_input)
    except ValueError:
      continue
    return result


def generate_integer(level):
    match level:
      case 1|2|3:
        pass
      case _:
        raise ValueError

    return random.randrange(0, 10**level)


if __name__ == '__main__':
  main()