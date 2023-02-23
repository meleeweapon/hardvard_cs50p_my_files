import tabulate
import csv
import os
import sys

def get_csv_reader(file):
  return csv.reader(file)

def main() -> None:
  argvs = sys.argv
  if len(argvs) < 2:
    sys.exit("too few arguments")
  elif len(argvs) > 2:
    sys.exit("too many arguments")
  
  file_path = argvs[1]
  if os.path.splitext(file_path)[1] != ".csv":
    sys.exit("file path must end with .csv")
  # if file_path.split(".")[-1] != "csv":
  #   sys.exit("file path must end with .csv")

  try:
    with open(file_path, "r") as csv_file:
      reader = csv.reader(csv_file)
      rows = list(reader)
  except FileNotFoundError:
    sys.exit("file not found")



  headers = rows.pop(0)

  print(tabulate.tabulate(rows, headers=headers, tablefmt="grid"))
    



if __name__ == '__main__':
  main()