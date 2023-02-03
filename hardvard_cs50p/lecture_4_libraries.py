import random
import statistics
import sys
import cowsay
import requests
import json

def main() -> None:
  # randomMain()
  # statistics_main()
  # command_line_arguments()
  # cowsay_main()
  itunes()

def random_main() -> None:
  coin = random.choice(["heads", "tails"])
  print(coin)

  number = random.randint(1, 10)
  print(number)

  animals = ["cat", "dog", "giraffe"]
  random.shuffle(animals)
  print(animals)

def statistics_main() -> None:
  mean = statistics.mean([75, 80, 90, 100])
  print(mean)

def command_line_arguments():
  # try:
  #   print(
  #     random.choice(sys.argv[1:])
  #     # sys.argv
  #   )
  # except IndexError:
  #   print("not enough command-line arguments were given")

  # if len(sys.argv) < 2:
  #   print("too few arguments")
  # elif len(sys.argv) >= 4:
  #   print("too many arguments")
  # else:
  #   print(
  #     random.choice(sys.argv[1:])
  #   )

  # check for errors
  if len(sys.argv) < 2:
    sys.exit("too few arguments")
  elif len(sys.argv) >= 4:
    sys.exit("too many arguments")
  
  # print the choice
  print(
    random.choice(sys.argv[1:])
  )


def cowsay_main() -> None:
  if len(sys.argv) == 2:
    cowsay.beavis(sys.argv[1])


def itunes() -> None:
  if len(sys.argv) != 2:
    sys.exit()
  
  response = requests.get(f"https://itunes.apple.com/search?entity=song&limit=50&term={sys.argv[1]}")
  response = response.json()
  # print(json.dumps(response, indent=2))
  for result in response["results"]:
    print(
      result["trackName"],
      ": ",
      result["trackPrice"],
      "$"
    )
  




if __name__ == "__main__":
  main()