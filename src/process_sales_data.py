import pandas as pd
from datetime import datetime
import os
import random

# Input folder
input_folder = "data/raw_data"
today_str = datetime.now().strftime("%Y-%m-%d")
base_filename = f"raw_sales_data_{today_str}"
filename = f"{base_filename}.xlsx"
filepath = os.path.normpath(os.path.join(input_folder, filename))

# Product info
product_details = {
    "Hats": {"Price": 5200, "Stock": random.randint(25, 100)},
    "Shirts": {"Price": 3750, "Stock": random.randint(25, 100)},
    "Pants": {"Price": 11390, "Stock": random.randint(25, 100)},
    "Shoes": {"Price": 7990, "Stock": random.randint(25, 100)}
}

# If file exists, use the latest version
version = 1
while not os.path.exists(filepath) and version < 10:
    filename = f"{base_filename}_v{version}.xlsx"
    filepath = os.path.normpath(os.path.join(input_folder, filename))
    version += 1

# Check if file exists
if not os.path.exists(filepath):
    print(f"Raw data file not found: {filepath}")
    exit()

# Load raw sales data
raw_df = pd.read_excel(filepath)

# Process data
processed_data = []
for _, row in raw_df.iterrows():
    product = row["Product"]
    price = row["Price"]
    stock = row["Stock Quantity"]
    units_sold = row["Units Sold"]
    revenue = units_sold * price
    remaining_stock = stock - units_sold


    processed_data.append({
        "Product": product,
        "Units Sold": units_sold,
        "Remaining Stock": remaining_stock,
        "Revenue (¥)": revenue
    })

# Create DataFrame
df = pd.DataFrame(processed_data)

# Output folder
output_folder = "data/sales_data"
os.makedirs(output_folder, exist_ok=True)
output_filename = f"sales_report_{today_str}.xlsx"
output_path = os.path.join(output_folder, output_filename)
df.to_excel(output_path, index=False)

print(f"Sales Report generated to {output_path}")
