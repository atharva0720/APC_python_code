# QUESTION 9


import pandas as pd

product_prices = {
    "Laptop": 50000,
    "Mobile": 25000,
    "Keyboard": 1200,
    "Mouse": 800,
    "Monitor": 12000
}

series = pd.Series(product_prices)

print("\nQUESTION 9")
print(series)

series = series * 1.10

print("\nPrices after 10% increase:")
print(series)

print("\nMost expensive product:")
print(series.idxmax(), series.max())

print("\nProducts costing more than 1000:")
print(series[series > 1000])


# ============================================================
