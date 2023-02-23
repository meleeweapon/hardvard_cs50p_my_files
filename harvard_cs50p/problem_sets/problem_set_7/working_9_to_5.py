import re

def main() -> None:
  test_cases = [
    ("9 AM to 5 PM", "09:00 to 17:00"),
    ("9:00 AM to 5:00 PM", "09:00 to 17:00"),
    ("10 PM to 8 AM", "22:00 to 08:00"),
    ("10:30 PM to 8:50 AM", "22:30 to 08:50"),
  ]
  for case, expected_result in test_cases:
    result = convert(case)
    if result != expected_result:
      print("failed: ", result, expected_result)
    else:
      print("success", case, result, sep="  ")

  test_cases_exceptions = [
    "9:60 AM to 5:60 PM",
    "9 AM - 5 PM",
    "09:00 AM - 17:00 PM",
  ]
  for case in test_cases_exceptions:
    try:
      convert(case)
    except ValueError:
      print("success", case, sep="  ")
    else:
      print("failed: ", case)


# def convert(x_to_y: str) -> str:
#   formatting = get_formatting_of_two(x_to_y)
#   first_time, second_time = get_times(x_to_y)
#   match formatting:
#     case "whole":
#       result_first_time = am_pm_whole_to_24(first_time)
#       result_second_time = am_pm_whole_to_24(second_time)
#     case "with_minutes":
#       result_first_time = am_pm_to_24(first_time)
#       result_second_time = am_pm_to_24(second_time)

#   return combine(result_first_time, result_second_time)

# def combine(first_time: str, second_time: str) -> str:
#   return f"{first_time} to {second_time}"

# def get_formatting_of_two(x_to_y: str) -> str:
#   """
#   returns "whole" if the first_time is written without minutes or "with_minutes" otherwise
#   raises ValueError if the two times are formatted differently
#   """
#   if "to" not in x_to_y:
#     raise ValueError
  
#   first_time, second_time = x_to_y.strip().split("to")
#   first_time = first_time.strip()
#   second_time = second_time.strip()

#   if ":" in first_time:
#     first_formatting = "with_minutes"
#   else:
#     first_formatting = "whole"
#   if ":" in second_time:
#     second_formatting = "with_minutes"
#   else:
#     second_formatting = "whole"
  
#   if first_formatting != second_formatting:
#     raise ValueError
  
#   return first_formatting


# def get_times(x_to_y: str) -> tuple[str, str]:
#   if "to" not in x_to_y:
#     raise ValueError
  
#   first_time, second_time = x_to_y.split("to")
#   return first_time.strip(), second_time.strip()


# def am_pm_to_24(time: str) -> str:
#   """
#   time must be formatted as either: 
#   X:XX AM
#   XX:XX AM
#   X:XX PM
#   XX:XX PM
#   """
#   hour_and_minute, am_or_pm = time.strip().upper().split(" ")
#   hour_and_minute = hour_and_minute.strip()
#   am_or_pm = am_or_pm.strip()

#   match am_or_pm:
#     case "AM" | "PM":
#       pass
#     case _:
#       raise ValueError
  
#   hour_and_minute_split = hour_and_minute.split(":")
#   if len(hour_and_minute_split) != 2:
#     raise ValueError
  
#   hour, minute = hour_and_minute_split
#   try:
#     hour = int(hour)
#     minute = int(minute)
#   except ValueError:
#     raise ValueError
#   if hour < 1 or hour > 12:
#     raise ValueError
#   if minute < 0 or minute > 59:
#     raise ValueError
  
#   if hour == 12:
#     if am_or_pm == "PM":
#       result_hour = 12
#       result_minute = minute
#     else:
#       result_hour = 0
#       result_minute = minute
#   else:
#     if am_or_pm == "PM":
#       result_hour = hour + 12
#       result_minute = minute
#     else:
#       result_hour = hour
#       result_minute = minute
  
#   return f"{result_hour:02}:{result_minute:02}"


# def am_pm_whole_to_24(time: str):
#   """
#   time must be formatted as either: 
#   X:XX AM
#   XX:XX AM
#   X:XX PM
#   XX:XX PM
#   """
#   hour, am_or_pm = time.strip().upper().split(" ")
#   hour = hour.strip()
#   am_or_pm = am_or_pm.strip()

#   match am_or_pm:
#     case "AM" | "PM":
#       pass
#     case _:
#       raise ValueError

#   try:
#     hour = int(hour)
#   except ValueError:
#     raise ValueError
#   minute = 0
  
#   if hour < 1 or hour > 12:
#     raise ValueError
#   if minute < 0 or minute > 59:
#     raise ValueError
  
#   if hour == 12:
#     if am_or_pm == "PM":
#       result_hour = 12
#       result_minute = minute
#     else:
#       result_hour = 0
#       result_minute = minute
#   else:
#     if am_or_pm == "PM":
#       result_hour = hour + 12
#       result_minute = minute
#     else:
#       result_hour = hour
#       result_minute = minute
  
#   return f"{result_hour:02}:{result_minute:02}"


def convert(x_to_y: str) -> str:
  # looks for colon to determine formatting
  if ":" in x_to_y:
    if times := re.search(r"^(1[0-2]|[1-9]):([0-5][0-9]) (AM|PM) to (1[0-2]|[1-9]):([0-5][0-9]) (AM|PM)$", x_to_y):
      first_hour, first_minute, first_am_pm, \
      second_hour, second_minute, second_am_pm = times.groups()
    else:
      raise ValueError

    return f"{am_pm_to_24(first_hour, first_minute, first_am_pm)} to {am_pm_to_24(second_hour, second_minute, second_am_pm)}"

  else:
    if times := re.search(r"^(1[0-2]|[1-9]) (AM|PM) to (1[0-2]|[1-9]) (AM|PM)$", x_to_y):
      first_hour, first_am_pm, \
      second_hour, second_am_pm = times.groups()
    else:
      raise ValueError
    
    return f"{am_pm_to_24(first_hour, '00', first_am_pm)} to {am_pm_to_24(second_hour, '00', second_am_pm)}"

def am_pm_to_24(hour, minute, am_pm) -> str:
  hour = int(hour)
  minute = int(minute)
  if hour == "12":
    if am_pm == "PM":
      result = f"{hour:02}:{minute:02}"
    else:
      result = f"00:{minute:02}"
  else:
    if am_pm == "PM":
      result = f"{hour + 12:02}:{minute:02}"
    else:
      result = f"{hour:02}:{minute:02}"
  
  return result


if __name__ == '__main__':
  main()