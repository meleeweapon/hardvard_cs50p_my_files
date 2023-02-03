import argparse
import sys
import pyfiglet

def main() -> None:
  parser = argparse.ArgumentParser(
    usage="no arguments for a random font, -f --font <font_name>"
  )
  parser.add_argument("-f", "--font", help="enter name of the font as argument")
  args = parser.parse_args()
  print(args.font)

  user_input = input("enter text: ")
  if args.font is None:
    # print(pyfiglet.print_figlet(user_input))
    pyfiglet.print_figlet(user_input)
  else:
    # print(pyfiglet.print_figlet(user_input, args.font))
    pyfiglet.print_figlet(user_input, args.font)


if __name__ == '__main__':
  main()