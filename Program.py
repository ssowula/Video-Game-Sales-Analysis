import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/vgsales.csv")
print(df.head(5))
print(df.info())
print(df.isnull().sum())

df=df.dropna()
print(df.isnull().sum())

topGames=df.sort_values(by=['Global_Sales'], ascending=False).head(5)
games=topGames['Name']
sale=topGames['Global_Sales']

plt.bar(games,sale)

plt.title("Top 5 games by sales")
plt.xlabel("Games")
plt.ylabel("Sales")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.show()