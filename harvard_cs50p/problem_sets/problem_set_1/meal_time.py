def main() -> None:
  user_input = input("what's the time?: ")
  print(meal_from_time(convert(user_input)))

# breakfast between 7:00 8:00
# lunch between 12:00 and 13:00
# dinner between 18:00 and 19:00
def meal_from_time(hour: float) -> str:
  if hour >= 7.0 and hour <= 8.0:
    return "breakfast"
  elif hour >= 12.0 and hour <= 13.0:
    return "lunch"
  elif hour >= 18.0 and hour <= 19.0:
    return "dinner"
  else:
    return ""


# #:## or ##:##
# 7:30 -> 7.5
def twenty_four_hour_to_float(time: str):
  hour, minute = time.split(":")
  return float(hour) + minute_to_hour(int(minute))

def minute_to_hour(minutes) -> float:
  return minutes / 60

def am_pm_to_float(time: str) -> float:
  time, am_pm = time.split(" ")
  if am_pm == "a.m.":
    hour, minute = time.split(":")
    hour = float(hour)
    minute = int(minute)
    if hour == 12.0:
      return 0.0  + minute_to_hour(minute)
    else:
      return hour + minute_to_hour(minute)
  elif am_pm == "p.m.":
    hour, minute = time.split(":")
    hour = float(hour)
    minute = int(minute)
    if hour == 12.0:
      return 0.0  + 12.0 + minute_to_hour(minute)
    else:
      return hour + 12.0 + minute_to_hour(minute)
  else:
    print("error: couldn't find 'a.m.' or 'p.m.'")

def is_am_pm(time: str) -> bool:
  return len(time.split(" ")) == 2

def convert(time: str):
  if is_am_pm(time):
    return am_pm_to_float(time)
  else:
    return twenty_four_hour_to_float(time)


if __name__ == '__main__':
  main()