import pandas as pd
from sklearn.linear_model import LinearRegression

def main() -> None:
  earthquake_data = pd.read_csv("earthquake_data.csv")

  x = earthquake_data[["Time", "Latitude", "Longitude"]]
  y = earthquake_data["Magnitude"]

  model = LinearRegression()
  model.fit(x, y)

  predictions = []
  for i in range(1000):
    new_data = pd.DataFrame({
      "Time": [1676314743000 + (100_000 * i)],
      "Latitude": [37.3095],
      "Longitude": [36.8262],
    })

    prediction = model.predict(new_data)
    predictions.append(prediction)

  print(*predictions, sep="\n")


if __name__ == '__main__':
  main()