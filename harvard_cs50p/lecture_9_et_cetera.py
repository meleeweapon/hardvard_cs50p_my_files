import sys
import argparse
import cowsay
import pyttsx3

def main() -> None:
  # sets()
  # bank()
  # meow()
  # meow_2()
  # meow_3()
  # unpacking()
  # unpacking_2()
  # yell()
  # gryffindors()
  # from_gryffindors()
  # enumeration()
  # generators()
  say()

def sets():
  students = [
    {"name": "hermoine", "house": "gryffindor"},
    {"name": "harry", "house": "gryffindor"},
    {"name": "ron", "house": "gryffindor"},
    {"name": "drako", "house": "slytherin"},
    {"name": "padma", "house": "ravenclaw"},
  ]

  # houses = []
  # for student in students:
  #   if student["house"] not in houses:
  #     houses.append(student["house"])
  # print(houses)

  houses = set()
  for student in students:
    houses.add(student["house"])
  print(houses)


# balance = 0
# def bank():
#   print("balance:", balance)
#   deposit(100)
#   withdraw(50)
#   print("balance:", balance)
# def deposit(amount):
#   global balance
#   balance += amount
# def withdraw(amount):
#   global balance
#   balance -= amount


class Account:
  def __init__(self) -> None:
    self._balance = 0
  
  @property
  def balance(self):
    return self._balance
  @balance.setter
  def balance(self, set):
    self._balance = set
  
  def deposit(self, amount):
    self.balance += amount

  def withdraw(self, amount):
    self.balance -= amount

def bank():
  account = Account()
  print(account.balance)
  account.deposit(100)
  account.withdraw(50)
  print(account.balance)


# MEOWS = 3
# def meow():
#   # for _ in range(3):
#   for _ in range(MEOWS):
#     print("meow")

class Cat:
  MEOWS = 3
  def meow(self):
    for _ in range(Cat.MEOWS):
      print("meow")

  # @classmethod
  # def meow(cls):
  #   for _ in range(cls.MEOWS):
  #     print("meow")
def meow():
  cat = Cat()
  cat.meow()
  # Cat.meow()


# mypy .\this_file
def meow_2() -> None:
  """alternative main function for meow"""
  def meow_type_safe(amount: int) -> str:
    """
    returns meow repeated amount times, every meow is followed by a new-line character, including the last one

    :param amount: number of times to meow
    :type amount: int
    :raise TypeError: if amount is not an int
    :return: string of repeated amount of 'meow's with every meow followed by a new-line character, including the last one
    :rtype: str
    """
    # for _ in range(amount):
    #   print("meow")
    return "meow\n" * amount
  
  number: int = int(input("meows: "))
  print(meow_type_safe(number))
  # meow_type_safe()


def meow_3():
  # if len(sys.argv) == 1:
  #   print("meow")
  # elif len(sys.argv) == 3:
  #   if sys.argv[1] == "-n":
  #     for _ in range(int(sys.argv[2])):
  #       print("meow")
  # else:
  #   print("usage: meows.py")

  parser = argparse.ArgumentParser(description="meow like a cat")
  parser.add_argument("-n", default=1, help="number of times to meow", type=int)
  args = parser.parse_args()

  for _ in range(args.n):
    print("meow")


def unpacking():
  def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts
  
  # coins = [100, 50, 25]
  coins = {"galleons": 100, "sickles": 50, "knuts": 25}
  print(total(**coins), "knuts")

def unpacking_2():
  def func(*args, **kwargs):
    print("positional", args)
    print("named", kwargs)
  
  func(100, 50, 25, awooga=69)

def yell():
  # def yell_map(*words):
  #   # return map(lambda word: word.upper(), words)
  #   return map(str.upper, words)
  
  # print(*list(yell_map("booba", "awooga")))

  words = ["booba", "awooga"]
  print([word.upper() for word in words])

def gryffindors():
  # students = [
  #   {"name": "hermoine", "house": "gryffindor"},
  #   {"name": "harry", "house": "gryffindor"},
  #   {"name": "ron", "house": "gryffindor"},
  #   {"name": "drako", "house": "slytherin"},
  #   {"name": "padma", "house": "ravenclaw"},
  # ]

  # listi = [
  #   student["name"]
  #   for student in students
  #   if student["house"] == "gryffindor"
  # ]

  # print(*listi)


  students = [
    {"name": "hermoine", "house": "gryffindor"},
    {"name": "harry", "house": "gryffindor"},
    {"name": "ron", "house": "gryffindor"},
    {"name": "drako", "house": "slytherin"},
    {"name": "padma", "house": "ravenclaw"},
  ]
  print(*map(
    lambda student: student["name"], 
    filter(
      lambda student: student["house"] == "gryffindor", 
      students)
      )
    )

def from_gryffindors():
  students = ["harry", "ron", "hermoine"]

  # students_with_houses = [{"name": student, "house": "gryffindor"} for student in students]
  students_with_houses = {student: "gryffindor" for student in students}

  print(students_with_houses)

def enumeration():
  students = ["harry", "ron", "hermoine"]

  # for index in range(len(students)):
  #   print(index + 1, students[index])

  for rank, student in enumerate(students, 1):
    print(rank, student)


def generators():
  # def fibonacci(limit):
  #   x = 0
  #   y = 1
  #   z = 1
  #   for _ in range(limit):
  #     x = y
  #     y = z
  #     z = x + y
  #     yield z
  
  # limit = int(input("how many fibonacci numbers?: "))
  # for number in fibonacci(limit):
  #   print(number, end="")


  def sheeps(limit):
    for number in range(limit):
      yield "🐑" * (number + 1)
  
  number_of_sheeps = int(input("how many sheeps?: "))
  for sheep in sheeps(number_of_sheeps):
    print(sheep)


def say():
  engine = pyttsx3.init()
  # user_input = input("what should i say?: ")
  user_input = "hehehe"
  cowsay.beavis(user_input)
  engine.say(user_input)
  engine.runAndWait()



if __name__ == '__main__':
  main()