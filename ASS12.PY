
# Experiment 12: Exploratory Data Analysis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a sample customer churn dataset
data = {
    "CustomerID": [1, 2, 3, 4, 5, 6],
    "Age": [24, 30, 25, np.nan, 40, 35],
    "MonthlyCharges": [500, 700, 450, 600, np.nan, 800],
    "Tenure": [12, 24, 6, 18, 36, 30],
    "Churn": ["No", "Yes", "No", "Yes", "No", "Yes"]
}

# Convert data into DataFrame
df = pd.DataFrame(data)

print("Original Dataset:")
print(df)


# Display dataset information
print("\nDataset Information:")
df.info()


# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())


# Fill missing numerical values with mean
df["Age"] = df["Age"].fillna(df["Age"].mean())

df["MonthlyCharges"] = df["MonthlyCharges"].fillna(
    df["MonthlyCharges"].mean()
)

print("\nDataset after handling missing values:")
print(df)


# Display descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe())


# Calculate average age
print("\nAverage Age:", df["Age"].mean())


# Calculate average monthly charges
print("Average Monthly Charges:",
      df["MonthlyCharges"].mean())


# Count customers who left and stayed
print("\nCustomer Churn Count:")
print(df["Churn"].value_counts())


# Visualize customer churn
df["Churn"].value_counts().plot(
    kind="bar",
    title="Customer Churn Analysis"
)

plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.show()


# Histogram of customer ages
plt.hist(df["Age"], bins=5, edgecolor="black")

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.show()


# Scatter plot: Age vs Monthly Charges
plt.scatter(df["Age"], df["MonthlyCharges"])

plt.title("Age vs Monthly Charges")
plt.xlabel("Age")
plt.ylabel("Monthly Charges")

plt.show()
