def main() -> None:
  mario()
  


def mario() -> None:
  print(pyramid(5))

def pyramid(height: int) -> str:
  result = ""
  for width_value in range(1, height + 1):
    result += row(height - width_value, " ") + row(width_value, "#") + "\n"
  return result[:-1]


def row(length: int, block: str) -> str:
  return block * length

if __name__ == "__main__":
  main()