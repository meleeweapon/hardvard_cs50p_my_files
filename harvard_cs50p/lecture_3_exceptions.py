def main():
  # try:
  #   user_input: int = int(input("what is x? "))
  #   print(f"x is {user_input}")
  # except ValueError:
  #   print("x is not an integer")

  # try:
  #   user_input: int = int(input("what is x? "))
  # except ValueError:
  #   print("x is not an integer")

  # print(f"x is {user_input}")

  # try:
  #   user_input: int = int(input("what is x? "))
  # except ValueError:
  #   print("x is not an integer")
  # else:
  #   print(f"x is {user_input}")

  # while True:
  #   try:
  #     user_input: int = int(input("what is x? "))
  #   except ValueError:
  #     print("x is not an integer")
  #   else:
  #     break

  # print(f"x is {user_input}")

  # def get_int() -> int:
  #   while True:
  #     try:
  #       user_input: int = int(input("what is x? "))
  #     except ValueError:
  #       print("x is not an integer")
  #     else:
  #       return user_input

  # print(f"x is {get_int()}")

  def get_int(prompt: str) -> int:
    while True:
      try:
        return int(input(prompt))
      except ValueError:
        pass

  print(f"x is {get_int('what is x? ')}")





if __name__ == "__main__":
  main()