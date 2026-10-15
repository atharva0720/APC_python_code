#1.Write a Python program using regular expressions to extract all digits from a given string

import re

def extract_digits(input_string):
   
    digits_list = re.findall(r'\d+', input_string)
    return digits_list

# Example usage:
text = "In 2026, the population increased by 1500 people across 3 cities."
result = extract_digits(text)

print("Extracted digits:", result)