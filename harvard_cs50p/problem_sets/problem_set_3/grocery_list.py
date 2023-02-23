def main() -> None:
  grocery_list = {}

  while True:
    user_input = input("enter item: ")
    if user_input == "\04":
      break

    # if user_input in grocery_list:
    #   grocery_list[user_input] += 1
    # else:
    #   grocery_list[user_input] = 1
    user_input = user_input.strip().lower()
    try:
      grocery_list[user_input] += 1
    except KeyError:
      grocery_list[user_input] = 1
  
  for key in sorted(grocery_list):
    print(f"{grocery_list[key]} {key.upper()}")



if __name__ == '__main__':
  main()