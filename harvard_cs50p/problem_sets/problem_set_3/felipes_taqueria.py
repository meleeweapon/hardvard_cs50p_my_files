def main() -> None:
  menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
  }

  print("menu: ")
  for key in menu:
    print(f"{key}: {menu[key]:.2f}")

  order_process(menu)


def order_process(menu) -> None:
  done = False
  total = 0.0
  while not done:
    user_input = input("enter a menu item: ").strip().lower()
    if user_input == "\04":
      break
    try:
      total += menu[user_input.title()]
    except KeyError:
      continue
    print(f"total: {total:.2f}$")
      

if __name__ == '__main__':
  main()