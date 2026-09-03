import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

# Number of orders
n_orders = 5000

# Customer IDs
customers = [f"CUST_{i:04d}" for i in range(1, 1001)]

# Product information
products = {
    "Electronics": [
        ("Wireless Headphones", 1999),
        ("Smart Watch", 2499),
        ("Bluetooth Speaker", 1599),
        ("Power Bank", 999)
    ],
    "Clothing": [
        ("T-Shirt", 599),
        ("Jeans", 1299),
        ("Hoodie", 999),
        ("Sneakers", 1999)
    ],
    "Home": [
        ("Table Lamp", 799),
        ("Bedsheet", 999),
        ("Coffee Maker", 2499),
        ("Storage Box", 499)
    ],
    "Beauty": [
        ("Face Wash", 299),
        ("Shampoo", 399),
        ("Body Lotion", 349),
        ("Perfume", 999)
    ],
    "Books": [
        ("Novel", 499),
        ("Programming Book", 899),
        ("Self Help Book", 599),
        ("Exam Guide", 699)
    ]
}

locations = {
    "Punjab": ["Patiala", "Mohali", "Ludhiana", "Amritsar"],
    "Haryana": ["Sonipat", "Panipat", "Gurugram", "Faridabad"],
    "Delhi": ["New Delhi"],
    "Chandigarh": ["Chandigarh"],
    "Himachal Pradesh": ["Shimla", "Solan"]
}

payment_modes = ["UPI", "Credit Card", "Debit Card", "Cash on Delivery"]

# Generate orders
data = []

start_date = datetime(2024, 1, 1)

for i in range(1, n_orders + 1):

    customer = np.random.choice(customers)

    category = np.random.choice(list(products.keys()))

    product, price = products[category][
        np.random.randint(len(products[category]))
    ]

    quantity = np.random.randint(1, 5)

    discount = np.random.choice(
        [0, 0.05, 0.10, 0.15, 0.20],
        p=[0.25, 0.25, 0.25, 0.15, 0.10]
    )

    order_date = start_date + timedelta(
        days=np.random.randint(0, 730)
    )

    state = np.random.choice(list(locations.keys()))

    city = np.random.choice(locations[state])

    payment = np.random.choice(payment_modes)

    revenue = quantity * price * (1 - discount)

    data.append([
        f"ORD_{i:05d}",
        customer,
        order_date,
        product,
        category,
        quantity,
        price,
        discount,
        round(revenue, 2),
        city,
        state,
        payment
    ])

# Create DataFrame
df = pd.DataFrame(data, columns=[
    "Order_ID",
    "Customer_ID",
    "Order_Date",
    "Product",
    "Category",
    "Quantity",
    "Unit_Price",
    "Discount",
    "Revenue",
    "City",
    "State",
    "Payment_Mode"
])

# Save dataset
df.to_csv("data/ecommerce.csv", index=False)

print("✅ ShopIntel dataset generated successfully!")
print(f"📊 Total Orders: {len(df)}")
print(f"👥 Total Customers: {df['Customer_ID'].nunique()}")
print(f"💰 Total Revenue: ₹{df['Revenue'].sum():,.2f}")
print("📁 File saved at: data/ecommerce.csv")