import re
plate = input("Enter vehicle registration number: ")
# 2 letters state, 2 digits district, 1-2 letters series, 4 digits unique number
pattern = r'^[A-Z]{2}\d{2}[A-Z]{1,2}\d{4}$'
if re.match(pattern, plate.upper()):
    print("Valid Indian Vehicle Registration Format")
else:
    print("Invalid Format")
