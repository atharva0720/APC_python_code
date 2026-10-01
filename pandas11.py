# QUESTION 11

import pandas as pd
student_attendance = {
    "Amit": 80,
    "Rahul": 70,
    "Sneha": 95,
    "Priya": 68,
    "Rohit": 92
}

series = pd.Series(student_attendance)

print("\nQUESTION 11")
print(series)

print("\nAverage Attendance:")
print(series.mean())

print("\nStudents below 75%:")
print(series[series < 75])

print("\nStudents above 90%:")
print(series[series > 90])

print("\nHighest Attendance:")
print(series.max())


# ============================================================
