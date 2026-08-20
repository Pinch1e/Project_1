import pandas as pd 

url = "https://www.football-data.co.uk/mmz4281/2425/E0.csv"

data = pd.read_csv(url)

print(data.head())
print(data.shape)
print(data.columns)
print(data["Home Team"])