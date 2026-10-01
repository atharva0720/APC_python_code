# QUESTION 15


import pandas as pd

df = pd.read_csv("weather.csv")

print("\nQUESTION 15")

print("\nMaximum Temperature:")
print(df["Temperature"].max())

print("\nMinimum Temperature:")
print(df["Temperature"].min())

print("\nAverage Temperature:")
print(df["Temperature"].mean())

print("\nRecords where temperature is above 35°C:")
print(df[df["Temperature"] > 35])

print("\nCity-wise average temperature:")
print(df.groupby("City")["Temperature"].mean())


# ============================================================
# END OF PANDAS PRACTICAL PROGRAMS
# ============================================================
