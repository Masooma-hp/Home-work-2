import pandas as pd

# 1. Load the dataset
df = pd.read_csv("labeled_data.csv")

# 2. Display the first five rows
print("First five rows:")
print(df.head())

# 3. Check dataset information
print("\nDataset information:")
df.info()

# 4. Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# 5. Remove duplicate records
df = df.drop_duplicates()

# 6. Clean column names
df.columns = df.columns.str.strip()

# 7. Clean text columns
for column in df.select_dtypes(include="object").columns:
    df[column] = df[column].str.strip()

# 8. Check remaining duplicates
print("\nRemaining duplicates:")
print(df.duplicated().sum())

# 9. Save the cleaned dataset
df.to_csv("final_cleaned_data.csv", index=False)

print("\nData cleaning completed successfully!")
print("Saved as final_cleaned_data.csv")