import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime


# CREATE OUTPUT FOLDER AUTOMATICALLY

os.makedirs("outputs", exist_ok=True)


# LOAD DATASET

df = pd.read_csv("dataset/customer__churn.csv")

print(" Dataset Loaded Successfully")
print(df.head())


# BASIC DATA CLEANING

df.columns = df.columns.str.strip()

# Convert TotalCharges to numeric if exists
if "TotalCharges" in df.columns:
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")


# KPI CALCULATIONS
total_customers = len(df)
churned_customers = df[df["Churn"] == "Yes"].shape[0]
churn_rate = (churned_customers / total_customers) * 100


# SAVE KPI SUMMARY

with open("outputs/churn_summary.txt", "w") as f:
    f.write("CUSTOMER CHURN ANALYSIS SUMMARY\n")
    f.write(f"Generated on: {datetime.now()}\n\n")
    f.write(f"Total Customers: {total_customers}\n")
    f.write(f"Churned Customers: {churned_customers}\n")
    f.write(f"Churn Rate: {churn_rate:.2f}%\n")

print(" KPI summary saved")


#  CHURN DISTRIBUTION

plt.figure()
df["Churn"].value_counts().plot(kind="bar", color=["green", "red"])
plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("outputs/churn_distribution.png")
plt.close()


#  CHURN BY CONTRACT TYPE

plt.figure()
df.groupby("Contract")["Churn"].value_counts().unstack().plot(
    kind="bar", stacked=True
)
plt.title("Churn by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Customers")
plt.tight_layout()
plt.savefig("outputs/churn_by_contract.png")
plt.close()


#  CHURN BY TENURE

plt.figure()
df.groupby("tenure")["Churn"].value_counts().unstack().fillna(0)["Yes"].plot()
plt.title("Churn Trend by Tenure")
plt.xlabel("Tenure (Months)")
plt.ylabel("Churned Customers")
plt.tight_layout()
plt.savefig("outputs/churn_by_tenure.png")
plt.close()

#  CHURN BY MONTHLY CHARGES

if "MonthlyCharges" in df.columns:
    plt.figure()
    df.boxplot(column="MonthlyCharges", by="Churn")
    plt.title("Monthly Charges vs Churn")
    plt.suptitle("")
    plt.xlabel("Churn")
    plt.ylabel("Monthly Charges")
    plt.tight_layout()
    plt.savefig("outputs/churn_by_monthly_charges.png")
    plt.close()


# FINISH

print("🎉 Customer Churn Analysis Completed Successfully!")
print("📂 Check the 'outputs' folder for results.")