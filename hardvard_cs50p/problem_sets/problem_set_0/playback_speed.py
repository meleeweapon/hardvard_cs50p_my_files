def main() -> None:
  # replace white space with triple dots ("...")
  user_input = input("write a few words: ")
  print("output:", user_input.replace(" ", "..."))


if __name__ == '__main__':
  main()