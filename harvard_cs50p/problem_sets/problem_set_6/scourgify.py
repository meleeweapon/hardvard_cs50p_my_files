import sys
import csv
import os

def main() -> None:
  argvs = sys.argv
  if len(argvs) < 3:
    sys.exit("too few arguments")
  elif len(argvs) > 3:
    sys.exit("too many arguments")
  
  target_file_path = argvs[1]
  destination_file_path = argvs[2]
  target_file_path_extension = os.path.splitext(target_file_path)[-1]
  destination_file_path_extension = os.path.splitext(destination_file_path)[-1]
  if target_file_path_extension != ".csv" or destination_file_path_extension != ".csv":
    sys.exit("path names must end with .csv")

  try:
    with open(target_file_path, "r") as target_file:
      target_file_rows = list(csv.DictReader(target_file))
  except FileNotFoundError:
    sys.exit("file doesn't exist")
  
  # destination_file_rows = []
  # for row in target_file_rows:
  #   des
  destination_file_rows = [
    {
      "first_name": row["name"].split(",")[1].strip(), 
      "last_name": row["name"].split(",")[0].strip(), 
      "house": row["house"],
    } 
    for row in target_file_rows
  ]

  with open(destination_file_path, "a") as destination_file:
    destination_writer = csv.DictWriter(
      destination_file, 
      ["first_name", "last_name", "house"],

    )
    destination_writer.writerows(destination_file_rows)




if __name__ == '__main__':
  main()