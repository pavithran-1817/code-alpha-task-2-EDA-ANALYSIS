
print("EDA PROJECT STARTED SUCCESSFULLY!")
import pandas as pd

# Load the dataset
df = pd.read_csv("books.csv")

# 1. Explore data structure
print("First 5 rows:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

# 2. Check missing values and duplicates
print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

# 3. Summary statistics
print("\nNumerical summary:")
print(df.describe())

# 4. Analyze book prices
print("\nAverage price:", df["Price (£)"].mean())
print("Highest price:", df["Price (£)"].max())
print("Lowest price:", df["Price (£)"].min())

# 5. Analyze ratings
print("\nRating distribution:")
print(df["Rating"].value_counts())

import matplotlib.pyplot as plt
print("VISUALIZATION STARTED")
import seaborn as sns

# 1. Book Price Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["Price (£)"], bins=10, kde=True)
plt.title("Distribution of Book Prices")
plt.xlabel("Book Price (£)")
plt.ylabel("Number of Books")
plt.show()

# 2. Rating Distribution
plt.figure(figsize=(8, 5))
sns.countplot(x="Rating", data=df)
plt.title("Distribution of Book Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Books")
plt.show()

# 3. Price Outlier Detection
plt.figure(figsize=(8, 5))
sns.boxplot(x=df["Price (£)"])
plt.title("Book Price Outlier Detection")
plt.xlabel("Book Price (£)")
plt.show()

from scipy.stats import spearmanr
print("HYPOTHESIS TEST STARTED")
sns.countplot(
    x="Rating",
    data=df,
    order=["One", "Two", "Three", "Four", "Five"]
)


# Convert ratings into numbers
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["Rating_Number"] = df["Rating"].map(rating_map)

# Spearman correlation
correlation, p_value = spearmanr(
    df["Price (£)"],
    df["Rating_Number"]
)

print("\n--- HYPOTHESIS TESTING ---")
print("Correlation:", correlation)
print("P-value:", p_value)

if p_value < 0.05:
    print("Significant relationship found.")
else:
    print("No statistically significant relationship found.")



# Spearman correlation test
correlation, p_value = spearmanr(
    df["Price (£)"],
    df["Rating_Number"]
)

print("\n--- Hypothesis Testing ---")
print("Correlation:", correlation)
print("P-value:", p_value)

if p_value < 0.05:
    print("Significant relationship found.")
else:
    print("No statistically significant relationship found.")

# STEP 4: Data Quality Analysis

print("\n--- DATA QUALITY ANALYSIS ---")

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# Check invalid prices
print("\nInvalid Prices:")
print(df[df["Price (£)"] <= 0])

# Check outliers using IQR
Q1 = df["Price (£)"].quantile(0.25)
Q3 = df["Price (£)"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = df[
    (df["Price (£)"] < lower_limit) |
    (df["Price (£)"] > upper_limit)
]

print("\nOutlier Books:")
print(outliers[["Book Name", "Price (£)"]])

print("\nTotal Outliers:", len(outliers))
print("\nEDA ANALYSIS COMPLETED!")