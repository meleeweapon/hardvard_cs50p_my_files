import requests
import sys

# look at json formatter

def main() -> None:
  try:
    bitcoins = float(sys.argv[1])
  except ValueError:
    print("invalid float value")
    sys.exit()
  except IndexError:
    print("no argument were given")
    sys.exit()
  

  try:
    coin_desk_response = requests.get(
      "https://api.coindesk.com/v1/bpi/currentprice.json"
    )
  except requests.RequestException:
    pass

  rate_float = coin_desk_response.json()["bpi"]["USD"]["rate_float"]
  final = bitcoins * rate_float
  print(f"${final:,.4f}")



if __name__ == '__main__':
  main()