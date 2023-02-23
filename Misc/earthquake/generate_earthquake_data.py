import csv
import re
import datetime

def main() -> None:
  # time in millisecond since epoch
  # latitude
  # longitude
  # magnitude

  # with open("earthquake_data.csv", "w") as file:
  #   csv_writer = csv.DictWriter(file, ["Time", "Latitude", "Longitude", "Magnitude"])
  #   csv_writer.writeheader()
  #   csv_writer.writerow({
  #     "Time": 1577836800, "Latitude": 38.8977, "Longitude": -77.0365, "Magnitude": 3.1
  #     })
  #   csv_writer.writerow({
  #     "Time": 1537866100, "Latitude": 58.8177, "Longitude": -71.0315, "Magnitude": 4.2
  #     })
  #   csv_writer.writerow({
  #     "Time": 9572835800, "Latitude": 18.8917, "Longitude": -73.0335, "Magnitude": 2.6
  #     })

  # with open("earthquake_data.csv", "r") as file:
  #   csv_reader = csv.DictReader(file)
  #   for row in csv_reader:
  #     print(row["Longitude"])



  with open("raw_earthquake_data.txt", "r") as file:
    data = list(file)
  
  tabs_to_spaces_data = [row.expandtabs(1).rstrip() for row in data]
  # no_location_data = [re.match(r"") for row in tabs_to_spaces_data]
  # print(tabs_to_spaces_data[19][19] == " ", f"this:{tabs_to_spaces_data[19][19]}", "space: ")
  # commaed_data = [row.replace(" ", ",") for row in tabs_to_spaces_data]
  row_arrays = [row.split(" ", 6) for row in tabs_to_spaces_data]


  # with open("version_1_earthquake_data.csv", "w") as file:
  #   csv_writer = csv.writer(file)
  #   csv_writer.writerow([
  #     "Date", "Time", "Latitude", "Longitude", "Depth", "Magnitude", "Location"
  #     ])
  #   for row in row_arrays:
  #     csv_writer.writerow(row)


  # with open("version_1_earthquake_data.csv", "r") as file:
  #   csv_reader = csv.DictReader(file, ["Date", "Time", "Latitude", "Longitude", "Depth", "Magnitude", "Location"])
  #   for row in csv_reader:
  #     print(row["Date"], row["Time"])

  # time = int(datetime.datetime.fromisoformat("2023.02.13".replace(".", "-")).timestamp() * 1000)
  # time = int(
  #   datetime.datetime.fromisoformat(
  #     "2023.02.13".replace(".", "-") + "T21:57:23" + "+03:00"
  #   ).timestamp() * 1000
  # )
  # print(time)
  # print(datetime.time.fromisoformat("2023.02.13".replace(".", "-")))
  
  # datetime.datetime.now().timestamp()


  # with open("earthquake_data.csv", "w") as file:
  #   csv_writer = csv.DictWriter(file, ["Time", "Latitude", "Longitude", "Magnitude"])
  #   csv_writer.writeheader()
  #   for row in booba:
  #     time = int(
  #       datetime.datetime.fromisoformat(
  #         row["Date"].replace(".", "-") + "T" + row["Time"] + "+03:00"
  #       ).timestamp() * 1000
  #     )
  #     # time = datetime.datetime.now().timestamp()
  #     csv_writer.writerow({
  #       "Time": time, "Latitude": row["Latitude"], "Longitude": row["Longitude"], "Magnitude": row["Magnitude"],
  #     })


  with open("version_1_earthquake_data.csv", "r") as readed_file:
    csv_reader = csv.DictReader(readed_file, ["Date", "Time", "Latitude", "Longitude", "Depth", "Magnitude", "Location"])
    with open("earthquake_data.csv", "w") as file:
      csv_writer = csv.DictWriter(file, ["Time", "Latitude", "Longitude", "Magnitude"])
      csv_writer.writeheader()
      is_first = True
      for row in csv_reader:
        if not is_first:
          time = int(
            datetime.datetime.fromisoformat(
              row["Date"].replace(".", "-") + "T" + row["Time"] + "+03:00"
            ).timestamp() * 1000
          )
          csv_writer.writerow({
            "Time": time, "Latitude": row["Latitude"], "Longitude": row["Longitude"], "Magnitude": row["Magnitude"],
          })
        else:
          is_first = False




if __name__ == '__main__':
  main()