def main() -> None:
  coke_price = 50
  # print(f"insert {coke_price} cents to get a coke")
  inserted_total = 0
  while inserted_total < 50:
    print(f"insert {coke_price - inserted_total} cents to get a coke")
    inputted_cents = input("insert coins only of these values: 25, 10 or 5 cents: ")
    match inputted_cents:
      case "25" | "10" | "5":
        inserted_total += int(inputted_cents)
  
  change = inserted_total - coke_price
  print(f"here's your coke, your change is {change} cents")



if __name__ == '__main__':
  main()