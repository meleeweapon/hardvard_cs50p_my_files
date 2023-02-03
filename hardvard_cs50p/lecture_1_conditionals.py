def main() -> None:
  # compare()
  # grade()
  # parity()
  house()

def compare() -> None:
  first_user_input: int = int(input("enter first number: "))
  second_user_input: int = int(input("enter first number: "))

  if first_user_input < second_user_input:
    print("first number is smaller than second number")
  # if first_user_input > second_user_input:
  #   print("first number is greater than second number")
  elif first_user_input > second_user_input:
    print("first number is greater than second number")
  # elif first_user_input == second_user_input:
  #   print("first number is equal to second number")
  else:
    print("first number is equal to second number")
  
  # if first_user_input < second_user_input or first_user_input > second_user_input:
  #   print("first number is not equal to second number")
  # else:
  #   print("first number is equal to second number")
  if first_user_input != second_user_input:
    print("first number is not equal to second number")
  else:
    print("first number is equal to second number")

def grade() -> None:
  grade: int = int(input("enter your grade: "))

  # if grade >= 90 and grade <= 100:
  #   print("your grade: A")
  # elif grade >= 80 and grade < 90:
  #   print("your grade: B")
  # elif grade >= 70 and grade < 80:
  #   print("your grade: C")
  # elif grade >= 60 and grade < 70:
  #   print("your grade: D")
  # else:
  #   print("your grade: F")

  # if 90 <= grade <= 100:
  #   print("your grade: A")
  # elif 80 <= grade < 90:
  #   print("your grade: B")
  # elif 70 <= grade < 80:
  #   print("your grade: C")
  # elif 60 <= grade < 70:
  #   print("your grade: D")
  # else:
  #   print("your grade: F")

  if grade >= 90:
    print("your grade: A")
  elif grade >= 80:
    print("your grade: B")
  elif grade >= 70:
    print("your grade: C")
  elif grade >= 60:
    print("your grade: D")
  else:
    print("your grade: F")

def parity() -> None:
  user_number = int(input("enter your number: "))

  def isEven(number: int) -> bool:
    # if number % 2 == 0:
    #   return True
    # else:
    #   return False

    # return True if number % 2 == 0 else False

    return number % 2 == 0

  
  if isEven(user_number):
    print("your number is even")
  else:
    print("your number is odd")

def house() -> None:
  name: str = input("enter your name: ")

  # if name == "harry":
  #   print("gryffindor")
  # elif name == "hermione":
  #   print("gryffindor")
  # elif name == "ron":
  #   print("gryffindor")
  # elif name == "drako":
  #   print("slytherin")
  # else:
  #   print("who?")

  # if name == "harry" or name == "hermione" or name == "ron":
  #   print("gryffindor")
  # elif name == "drako":
  #   print("slytherin")
  # else:
  #   print("who?")

  match name:
    case "harry" | "hermoine" | "ron":
      print("gryffindor")
    case "drako":
      print("slytherin")
    case _:
      print("who?")






if __name__ == "__main__":
  main()