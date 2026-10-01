# QUESTION 8


import pandas as pd
employee_salary = {
    "Atharva": 55000,
    "Aniket": 300,
    "Sudarshan":5000,
    "Sanjana": 45000,
    "Tanisha": 65000,
}


series = pd.Series(employee_salary)

print(series)


print("\nHighest Salary:")
print(series.max())

print("\nLowest Salary:")
print(series.min())

print("\nAverage Salary:")
print(series.mean())

print("\nEmployees earning more than 50000:")
print(series[series > 50000])


