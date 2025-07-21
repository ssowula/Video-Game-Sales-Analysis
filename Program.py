import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/vgsales.csv")
print(df.head(5))
print(df.info())
print(df.isnull().sum())

df=df.dropna()
print(df.isnull().sum())

