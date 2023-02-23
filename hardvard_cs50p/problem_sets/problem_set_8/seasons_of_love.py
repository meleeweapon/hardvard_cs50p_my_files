import datetime
import sys
import inflect

def main() -> None:
  # get a date in YYYY-MM-DD format
  # return total minutes from midnight of the day to midnight of today

  # print(sing(total_minutes_to_today(format_input("2022-02-10"))))
  print("date must be formatted as YYYY-MM-DD or Month DD, YYYY or MM/DD/YYYY")
  user_input = input("enter date: ")
  print(sing(total_minutes_to_today(format_input(user_input))))


def sing(minutes: str) -> str:
  return inflect.engine() \
    .number_to_words(minutes, andword="") + " minutes"

def total_minutes_to_today(from_date: str) -> int:
  return total_minutes(from_date, str(datetime.date.today()))

def total_minutes(from_date: str, to_date: str) -> int:
  try:
    from_year, from_month, from_day = from_date.split("-")
    to_year, to_month, to_day = to_date.split("-")
    difference = datetime.date(int(to_year)  , int(to_month)  , int(to_day)) \
               - datetime.date(int(from_year), int(from_month), int(from_day))
  except ValueError:
    sys.exit("incorrect formatting")
  return days_to_minutes(difference.days)

def days_to_minutes(days: int) -> int:
  return days * 24 * 60

def middle_endian_to_iso_8601(month: int, day: int, year: int) -> str:
  return f"{year:04}-{month:02}-{day:02}"

def convert_date(date: str) -> str:
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
  if "/" in date:
    month, day, year = date.split("/")
  else:
    month, day, year = date.split(" ")
    if "," in day:
      day = day.replace(",", "")
    month = months[month.lower().title()]

  day = int(day)
  month = int(month)
  year = int(year)
  
  if day > 31:
    raise ValueError
  if month > 12:
    raise ValueError
    
  return middle_endian_to_iso_8601(month, day, year)

def format_input(user_input: str) -> str:
  if "-" not in user_input:
    try:
      return convert_date(user_input)
    except ValueError:
      sys.exit("incorrect formatting")
  return user_input


if __name__ == '__main__':
  main()