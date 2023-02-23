def main() -> None:
  # meow()
  # meowVariably()
  # meow_2()
  # meow_3()
  # hogwarts()
  # hogwarts_2()
  # hogwarts_3()
  # hogwarts_4()
  mario()


def meow() -> None:
  # print("meow")
  # print("meow")
  # print("meow")
  
  # i: int = 100
  # while i >= 0:
  #   print("meow")
  #   i -= 1

  # for index in [0, 1, 2]:
  #   print("meow")

  # for _ in range(3):
  #   print("meow")

  print("meow\n" * 3, end="")


def meowVariably() -> None:
  user_inputted_meow_amount: int = insist_positive_int()

  for _ in range(user_inputted_meow_amount):
    print("meow")

# def insist_positive_int() -> int:
#   result: int = int(input("how many times should the cat meow?: "))
#   while result < 0:
#     print("input has to be a positive value")
#     result = int(input("how many times should the cat meow?: "))
#   return result

# def insist_positive_int() -> int:
#   while True:
#     result: int = int(input("how many times should the cat meow?: "))
#     if result < 0:
#       print("input has to be a positive value")
#       continue
#     else:
#       break
#   return result

def insist_positive_int() -> int:
  while True:
    result: int = int(input("how many times should the cat meow?: "))
    if result >= 0:
      return result
    else:
      print("input has to be a positive value")


def meow_2() -> None:
  amount: int = insist_positive_int()
  for meow in meow_func(amount):
    print(meow)

def meow_func(amount: int) -> str:
  for _ in range(amount):
    yield "meow"



def meow_3() -> None:
  amount: int = insist_positive_int()
  meow_func_2(amount)

def meow_func_2(amount: int) -> None:
  for _ in range(amount):
    print("meow")


def hogwarts() -> None:
  students: list[str] = ["harry", "hermoine", "ron"]

  # print(students[0])
  # print(students[1])
  # print(students[2])

  # for index in range(len(students)):
  #   print(index + 1, students[index])

  for student in students:
    print(student)


def hogwarts_2() -> None:
  students: list[str] = ["harry", "hermoine", "ron", "drako"]
  locations: list[str] = ["gryffindor", "gryffindor", "gryffindor", "slytherin"]
  test = zip(students, locations)
  for student, location in test:
    print(student, location)

def hogwarts_3() -> None:
  students: dict = {
    "harry":    "gryffindor",
    "hermoine": "gryffindor",
    "ron":      "gryffindor",
    "drako":    "slytherin",
  }

  for student in students:
    print(student, students[student])


def hogwarts_4() -> None:
  students: list[dict] = [
    {"name": "harry", "house": "gryffindor", "patronus": "stag"},
    {"name": "hermoine", "house": "gryffindor", "patronus": "otter"},
    {"name": "ron", "house": "gryffindor", "patronus": "terrier"},
    {"name": "drako", "house": "slytherin", "patronus": "none"},
  ]

  for student in students:
    print(
      student["name"], 
      student["house"], 
      student["patronus"], 
      sep=", "
    )


def mario() -> None:
  height: int = 4
  width: int = 3
  print(pipe(height, width))

def pipe(height: int, width: int) -> str:
  result: str = ""
  for _ in range(height):
    for _ in range(width):
      result += "#"
    result += "\n"
  return result[:-1]





if __name__ == "__main__":
  main()