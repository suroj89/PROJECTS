import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector
import os
from datetime import datetime

########################################
# AUTO CREATE outputs FOLDER


if not os.path.exists("outputs"):
    os.makedirs("outputs")




# DATABASE CONNECTION

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Suroj@725",
    database="sales_db"
)

# LOAD DATA

df = pd.read_sql("SELECT * FROM sales_data", conn)


total_sales = df["sales"].sum()
total_profit = df["profit"].sum()
avg_margin = (df["profit"] / df["sales"]).mean() * 100

# summary.txt

with open("outputs/summary.txt", "w") as f:
    f.write("SALES PERFORMANCE SUMMARY\n")
    f.write(f"Generated on: {datetime.now()}\n\n")
    f.write(f"Total Sales: {total_sales}\n")
    f.write(f"Total Profit: {total_profit}\n")
    f.write(f"Average Profit Margin: {avg_margin:.2f}%\n")


#sales_by_region.png

plt.figure()
df.groupby("region")["sales"].sum().plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("outputs/sales_by_region.png")
plt.close()


# sales_by_product.png

plt.figure()
df.groupby("product")["sales"].sum().plot(kind="bar")
plt.title("Sales by Product")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/sales_by_product.png")
plt.close()


# monthly_sales.png

df["order_date"] = pd.to_datetime(df["order_date"])
df["month"] = df["order_date"].dt.month

plt.figure()
df.groupby("month")["sales"].sum().plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("outputs/monthly_sales.png")
plt.close()

conn.close()

print("✅ All outputs auto-created successfully!")
