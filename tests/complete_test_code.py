import pandas as pd
import random
from datetime import datetime
import os
import openpyxl

# Sample product list
products = {
    "Hats": 5200,
    "Shirts": 3750,
    "Pants": 11390,
    "Shoes": 7990
}

# Fixed quantity
stock_quantity = 100

# Generate random sales data
sales_data = []
for product, price in products.items():
    unit_sold = random.randint(0, stock_quantity) # Random sales up to the stock amount.
    remaining_stock = stock_quantity - unit_sold
    revenue = unit_sold * price
    sales_data.append({
        "Product": product,
        "Price (¥)": price,
        "Stock Quantity": stock_quantity,
        "Unit Sold": unit_sold,
        "Remaining Stock": remaining_stock,
        "Revenue (¥)": revenue
    })

# Create DataFrame - For storing table data
df = pd.DataFrame(sales_data)

# Output folder definition
output_folder = "output_data"
os.makedirs(output_folder, exist_ok=True) # Creates a folder if it doesn't exist

# Create filename with today's date and the file
today_str = datetime.now().strftime("%Y-%m-%d")
base_filename = f"sales_data_{today_str}"
filename = f"{base_filename}.xlsx"
filepath = os.path.join(output_folder, filename)

# Prevent outputted files from overwriting existing files
version = 1
while os.path.exists(filepath):
    filename = f"{base_filename}_v{version}.xlsx"
    filepath = os.path.join(output_folder, filename)
    version += 1

# Save to excel
df.to_excel(filepath, index=False, engine="openpyxl")
print(f"Generated {filepath}")

