def main() -> None:
  user_input = int(input("input mass: "))
  print("joules: ", massToJoules(user_input))

SPEED_OF_LIGHT_IN_METERS_PER_SECOND = 300_000_000

def massToJoules(mass: int) -> int:
  # mass in kilograms
  # energy in joules
  return mass * (SPEED_OF_LIGHT_IN_METERS_PER_SECOND * SPEED_OF_LIGHT_IN_METERS_PER_SECOND)

if __name__ == '__main__':
  main()