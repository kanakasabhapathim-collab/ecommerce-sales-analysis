import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# eCommerce sales dataset
data = {
    "Order_ID": [
        1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010,
        1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020,
        1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030
    ],
    "Product": [
        "Laptop", "Phone", "Headphones", "Tablet", "Keyboard",
        "Phone", "Laptop", "Mouse", "Headphones", "Tablet",
        "Keyboard", "Phone", "Laptop", "Mouse", "Tablet",
        "Headphones", "Phone", "Keyboard", "Laptop", "Mouse",
        "Tablet", "Phone", "Headphones", "Laptop", "Keyboard",
        "Mouse", "Tablet", "Phone", "Laptop", "Headphones"
    ],
    "Category": [
        "Electronics", "Electronics", "Accessories", "Electronics",
        "Accessories", "Electronics", "Electronics", "Accessories",
        "Accessories", "Electronics", "Accessories", "Electronics",
        "Electronics", "Accessories", "Electronics", "Accessories",
        "Electronics", "Accessories", "Electronics", "Accessories",
        "Electronics", "Electronics", "Accessories", "Electronics",
        "Accessories", "Accessories", "Electronics", "Electronics",
        "Electronics", "Accessories"
    ],
    "Quantity": [
        2, 3, 5, 2, 4, 1, 3, 6, 2, 3,
        5, 2, 1, 8, 2, 4, 3, 6, 2, 5,
        4, 1, 7, 2, 3, 9, 1, 4, 1, 6
    ],
    "Price": [
        50000, 20000, 2000, 15000, 1500,
        22000, 48000, 800, 2500, 16000,
        1200, 21000, 52000, 750, 14500,
        1800, 19500, 1300, 49000, 900,
        15500, 23000, 2200, 51000, 1600,
        850, 14000, 20500, 53000, 1900
    ],
    "Region": [
        "South", "North", "East", "West", "South",
        "East", "North", "South", "West", "East",
        "North", "South", "West", "East", "North",
        "South", "West", "East", "South", "North",
        "West", "South", "East", "North", "West",
        "South", "East", "North", "West", "South"
    ],
    "Payment_Method": [
        "UPI", "Card", "UPI", "Cash", "Card",
        "UPI", "Card", "Cash", "UPI", "Card",
        "Cash", "UPI", "Card", "UPI", "Cash",
        "Card", "UPI", "Cash", "Card", "UPI",
        "Cash", "Card", "UPI", "Card", "Cash",
        "UPI", "Card", "UPI", "Cash", "Card"
    ]
}

df = pd.DataFrame(data)

# 2. Calculate sales revenue
df["Revenue"] = df["Quantity"] * df["Price"]

# 3. Analyse sales using NumPy
total_sales = np.sum(df["Revenue"])
average_sales = np.mean(df["Revenue"])

print("Total Sales:", total_sales)
print("Average Sales per Record:", average_sales)

# 4. Find the best-selling product by units
product_sales = df.groupby("Product")["Quantity"].sum()

print("\nQuantity Sold by Product:")
print(product_sales)

print("\nBest-Selling Product:")
print(product_sales.idxmax())

# 5. Display final dataset
print("\nFinal Sales Data:")
print(df)

# 6. Save results
# df.to_csv("ecommerce_sales.csv", index=False)
df.to_csv(r"F:\AAAAAAAAAAAAP PREP\Sabha_DA\Data\Python\Project\Ecommerce\ecommerce_sales.csv", index=False)


# 7. Create sales chart
plt.bar(product_sales.index, product_sales.values)
plt.title("eCommerce Product Sales")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.tight_layout()
plt.savefig("ecommerce_chart.png")
plt.show()