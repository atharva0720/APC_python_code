# QUESTION 3
# Create a dictionary containing Product ID, Product Name,


import pandas as pd

products = {
    "Product_ID": [101, 102, 103, 104, 105],
    "Product_Name": ["Laptop", "Mobile", "Keyboard", "Mouse", "Monitor"],
    "Category": ["Electronics", "Electronics", "Accessories", "Accessories", "Electronics"],
    "Price": [50000, 25000, 1500, 800, 12000],
    "Quantity": [2, 3, 10, 15, 4]
}

df = pd.DataFrame(products)

print("\nQUESTION 3")
df["Total_Amount"] = df["Price"] * df["Quantity"]

print(df)

print("\nProduct with highest total sales:")
print(df.loc[df["Total_Amount"].idxmax()])


# ============================================================
