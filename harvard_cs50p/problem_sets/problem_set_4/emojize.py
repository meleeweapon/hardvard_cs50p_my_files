import emoji

def main() -> None:
  user_input = input("enter alias: ")
  print(emoji.emojize(user_input, language="alias"))


if __name__ == '__main__':
  main()