# QUESTION 10
# Create a Pandas Series using a dictionary where patient IDs

import pandas as pd


patient_ages = {
    101: 65,
    102: 45,
    103: 70,
    104: 30,
    105: 62
}

series = pd.Series(patient_ages)

print("\nQUESTION 10")
print(series)

print("\nAverage Age:")
print(series.mean())

print("\nOldest Patient:")
print(series.idxmax(), series.max())

print("\nYoungest Patient:")
print(series.idxmin(), series.min())

print("\nPatients above 60 years:")
print(series[series > 60])


# ============================================================
