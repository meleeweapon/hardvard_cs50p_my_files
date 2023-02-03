import inflect

def main() -> None:
  inflector = inflect.engine()

  all_names = []
  while True:
    user_input = input("name: ")
    if user_input == "\04":
      break
    all_names.append(user_input)
  
  # formatted_names = all_names.pop(0)
  # for ind, name in enumerate(all_names):
  #   if ind == len(all_names) - 1:
  #     formatted_names = formatted_names + " and " + name
  #   else:
  #     formatted_names = formatted_names + ", " + name

  formatted_names = inflector.join(all_names)

  print(f"adieu, adieu, to {formatted_names}")


if __name__ == '__main__':
  main()