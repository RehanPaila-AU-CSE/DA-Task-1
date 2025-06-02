# mall_customer_cleaning.py

import pandas as pd

# 1. Load the dataset
df = pd.read_csv("Mall_Customers.csv")  # Make sure this file is in your working directory

# 2. Initial Exploration
print("Initial data preview:")
print(df.head())
print("\nInfo before cleaning:")
print(df.info())
print("\nMissing values per column:")
print(df.isnull().sum())

# 3. Handle missing values
# Option 1: Drop rows with any nulls (you could also fill them depending on context)
df = df.dropna()

# 4. Remove duplicates
df = df.drop_duplicates()

# 5. Standardize text values (Gender column)
if 'Gender' in df.columns:
    df['Gender'] = df['Gender'].str.strip().str.lower()

# 6. Convert any date columns (not in this dataset by default, but included for general use)
# Example: if there were a 'JoinDate' column
# df['JoinDate'] = pd.to_datetime(df['JoinDate'], errors='coerce')

# 7. Rename columns to lowercase and use underscores instead of spaces
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# 8. Fix data types
# Convert 'age' and 'annual_income_(k$)' to numeric, just in case
if 'age' in df.columns:
    df['age'] = pd.to_numeric(df['age'], errors='coerce').astype(int)

if 'annual_income_(k$)' in df.columns:
    df['annual_income_(k$)'] = pd.to_numeric(df['annual_income_(k$)'], errors='coerce')

# 9. Final preview and export
print("\nCleaned dataset preview:")
print(df.head())

# 10. Export to new CSV file
df.to_csv("cleaned_mall_customers.csv", index=False)
print("\nCleaned dataset saved as 'cleaned_mall_customers.csv'.")
