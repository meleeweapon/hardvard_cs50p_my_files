import sys
import os

def main() -> None:
  argvs = sys.argv
  if len(argvs) < 2:
    sys.exit("Too few command-line arguments")
  elif len(argvs) > 2:
    sys.exit("Too many command-line arguments")

  if os.path.splitext(argvs[1])[-1] != ".py":
    sys.exit("argument must end with .py")
  
  file_path = argvs[1]
  
  try:
    file = open(file_path, "r")
  except FileNotFoundError:
    sys.exit("file does not exist")


  # ooga
  # booga

  
  print(lines_of_code(file))

  file.close()


def lines_of_code(file):
  lines_of_code = 0
  for line in file:
    line = line.strip()
    if not (len(line) < 1 or line[0] == "#"):
      lines_of_code += 1
  return lines_of_code

    


if __name__ == '__main__':
  main()