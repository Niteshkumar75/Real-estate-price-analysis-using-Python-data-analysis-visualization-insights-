from statistics import correlation

import pandas as pd

data = {
    "City": ["Berlin", "Berlin", "Munich", "Munich", "Hamburg", "Hamburg"],
    "Size_sqm": [50, 70, 60, 80, 55, 75],
    "Rooms": [2, 3, 2, 4, 2, 3],
    "Price":[300000, 450000, 400000, 650000, 320000, 500000]
}
df = pd.DataFrame(data)

print(df)

print(df.info())
print(df.isnull().sum())


avg_price = df.groupby("City")["Price"].mean()
print(avg_price)

print(df[["Size_sqm", "Price"]])

Price_per_room = df["Price"] / df["Rooms"]
print(Price_per_room)

import matplotlib.pyplot as plt

avg_price.plot(kind="bar")
plt.title("Average House Price by City")
plt.xlabel("City")
plt.ylabel("Price (€)")
plt.show()

plt.scatter(df["Size_sqm"], df["Price"])
plt.xlabel("Size (sqm)")
plt.ylabel("Price (€)")
plt.title("Size vs Price")
plt.show()


correlation = df.corr(numeric_only=True)
print(correlation)