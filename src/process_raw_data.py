import pandas as pd
import random
from datetime import datetime
import os
import openpyxl

# Sample product list and prices
product_prices = {
    "Hats": 5200,
    "Shirts": 3750,
    "Pants": 11390,
    "Shoes": 7990
}

# Generate randomized stock and sales
sales_data = []
for product, price in product_prices.items():
    stock = random.randint(25, 100)
    units_sold = random.randint(0, stock)
    sales_data.append({
        "Product": product,
        "Price": price,
        "Stock Quantity": stock,
        "Units Sold": units_sold
    })

# Create DataFrame - For storing table data
df = pd.DataFrame(sales_data)

# Output folder definition
output_folder = "data/raw_data"
os.makedirs(output_folder, exist_ok=True) # Creates a folder if it doesn't exist

# Create filename with today's date
today_str = datetime.now().strftime("%Y-%m-%d")
base_filename = f"raw_sales_data_{today_str}"
filename = f"{base_filename}.xlsx"
filepath = os.path.join(output_folder, filename)

# Prevent outputted files from overwriting existing files
version = 1
while os.path.exists(filepath):
    filename = f"{base_filename}_v{version}.xlsx"
    filepath = os.path.join(output_folder, filename)
    version += 1

# Save to excel
df.to_excel(filepath, index=False)
print(f"Generated raw data to {filepath}")
