def main() -> None:
  months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
  ]
  months = {month: str(number + 1) for number, month in enumerate(months)}

  while True:
    user_input = input("enter a date: ")
    result = convert_date(user_input, months)
    if result == "invalid date":
      print("invalid date")
      continue
    else:
      print(result)
      break


def middle_endian_to_iso_8601(month: int, day: int, year: int) -> str:
  return f"{year:04}-{month:02}-{day:02}"

def convert_date(date: str, months: dict) -> str:
  if "/" in date:
    try:
      month, day, year = date.split("/")
    except ValueError:
      return "invalid date"
  else:
    try:
      month, day, year = date.split(" ")
    except ValueError:
      return "invalid date"
    day = day[:-1]
    month = months[month.lower().title()]

  try:
    day = int(day)
    month = int(month)
    year = int(year)
  except ValueError:
    return "invalid date"
  
  if day > 31:
    return "invalid date"
  if month > 12:
    return "invalid date"
    
  result = middle_endian_to_iso_8601(month, day, year)
  return result


if __name__ == '__main__':
  main()