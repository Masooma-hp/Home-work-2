import pandas as pd

# 1. Load the dataset
df = pd.read_csv("week02_homework/labeled_data_cleaned.csv", nrows=1000, low_memory=False)

# 2. Display the first five rows
print("First five rows:")
print(df.head())

# 3. Check the dataset information
print("\nDataset information:")
print(df.info())

# 4. Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# 5. Remove duplicate records
df = df.drop_duplicates()

# 6. Remove unnecessary spaces from column names
df.columns = df.columns.str.strip()

# 7. Clean text columns
for column in df.select_dtypes(include="object").columns:
    df[column] = df[column].str.strip()

# 8. Check the number of duplicate records
print("\nRemaining duplicates:")
print(df.duplicated().sum())

# 9. Save the cleaned dataset
df.to_csv("week02_homework/final_cleaned_data.csv", index=False)

print("\nData cleaning completed successfully!")
print("Cleaned dataset saved as week02_homework/final_cleaned_data.csv")

# 10. Check data types
print("\nData types:")
print(df.dtypes)

# 11. Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# 12. Check negative numeric values
print("\nNegative values in numeric columns:")
numeric_df = df.select_dtypes(include="number")
print((numeric_df < 0).sum())

# 13. Check categorical values
print("\nCategorical columns:")
for column in df.select_dtypes(include="object").columns:
    print(f"\n{column}:")
    print(df[column].value_counts().head(10))

# 14. Check dataset shape
print("\nDataset shape:")
print(df.shape)

# 15. Check column names
print("\nColumn names:")
print(df.columns.tolist())

# 16. Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# 17. Check data types
print("\nData types:")
print(df.dtypes)

# 18. Analyze missing wholesale prices
print("\nMissing wholesale prices:")
print(df[df["Wholesale Price (RMB/kg)"].isnull()].head(10))

# 19. Summary of numerical columns
print("\nNumerical summary:")
print(df.describe())

# 20. Check negative values in relevant columns
columns_to_check = [
    "Quantity_Sold_(kilo)",
    "Unit Selling Price (RMB/kg)",
    "Wholesale Price (RMB/kg)",
    "Loss Rate (%)"
]

print("\nNegative values:")
for column in columns_to_check:
    print(column, (df[column] < 0).sum())


# 21. Inspect negative selling prices
negative_prices = df[df["Unit Selling Price (RMB/kg)"] < 0]

print("\nRows with negative selling prices:")
print(negative_prices[
    [
        "ID",
        "Item Code",
        "Item Name_x",
        "Category Name",
        "Unit Selling Price (RMB/kg)"
    ]
].head(20))

print("\nNumber of negative selling prices:")
print(len(negative_prices))

# 22. Correct invalid negative selling prices

price_column = "Unit Selling Price (RMB/kg)"

# Count negative prices before correction
negative_before = (df[price_column] < 0).sum()
print("\nNegative prices before correction:", negative_before)

# Mark negative selling prices as missing values
df.loc[df[price_column] < 0, price_column] = float("nan")

# Count negative prices after correction
negative_after = (df[price_column] < 0).sum()
print("Negative prices after correction:", negative_after)

# Check missing values in selling price
print("Missing selling prices:", df[price_column].isna().sum())

# 23. Save the final cleaned dataset

df.to_csv(
    "week02_homework/final_cleaned_data.csv",
    index=False
)

print("\nFinal dataset saved successfully!")
print("File: week02_homework/final_cleaned_data.csv")