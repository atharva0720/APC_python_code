# QUESTION 8


import pandas as pd
employee_salary = {
    "Amit": 55000,
    "Rahul": 48000,
    "Sneha": 72000,
    "Priya": 45000,
    "Rohit": 65000,
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
