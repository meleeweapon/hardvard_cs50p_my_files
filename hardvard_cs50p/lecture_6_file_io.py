import csv
import sys
from PIL import Image

def main() -> None:
  # print(hello_all("ron", "harry", "hermoine"))

  # names = []
  # for _ in range(3):
  #   names.append(input("write a name: "))
  
  # print(*sorted(names), sep=", ")

  # names_write()
  # names_csv()
  # students()
  costumes()


def hello_all(*names: str) -> str:
  return "hello " + ", ".join(names)

def names_write() -> None:
  # name = input("enter your name: ")

  # file = open("names.txt", "w")
  # file = open("names.txt", "a")
  # file.write(name + "\n")
  # file.close

  # with open("names.txt", "a") as file:
  #   file.write(name + "\n")
  
  # with open("names.txt", "r") as file_to_read:
  #   all_names = file_to_read.readlines()
  #   for line in all_names:
  #   #   print(f"hello, {line}", end="")
  #     print(f"hello, {line.rstrip()}")
  #   # all_names = file_to_read.read()
  #   # print(all_names)

  # with open("names.txt", "r") as file_to_read:
  #   for line in file_to_read:
  #     print(f"hello, {line.rstrip()}")

  # with open("names.txt") as file_to_read:
  #   for line in sorted(file_to_read):
  #     print(f"hello, {line.rstrip()}")

  all_names = []
  with open("names.txt") as file_to_read:
    all_names = file_to_read.readlines()
  for line in sorted(all_names):
    print(f"hello, {line.rstrip()}")

def names_csv() -> None:
  with open("names.csv") as file:
    for line in file:
      print(line.rstrip())

def students() -> None:
  with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["home", "name"])
    writer.writerow({"home": "booba", "name": "awooga",})
  
  students = []
  with open("students.csv") as file:
    # for line in sorted(file):
      # row = line.rstrip().split(",")
      # print(f"{row[0]} is in {row[1]}")

      # name, location = line.rstrip().split(",")
      # print(f"{name} is in {location}")

  #     name, location = line.rstrip().split(",")
  #     students.append(f"{name} is in {location}")
  # print(*sorted(students))

  #   for line in file:
  #     # this gets complicated
  #     name, home = line.rstrip().split(",")
  #     students.append({
  #       "name": name,
  #       "home": home,
  #     })
  # for student in sorted(students, key=lambda student: student["name"]):
  #   print(f"{student['name']} is from {student['home']}")

    reader = csv.DictReader(file)
    for row in reader:
      students.append({"name": row["name"], "home": row["home"]})

  for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
  

def costumes() -> None:
  # give costume1.gif and costume2.gif as cl arguments
  images = []
  for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)
  images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200
  )




if __name__ == '__main__':
  main()