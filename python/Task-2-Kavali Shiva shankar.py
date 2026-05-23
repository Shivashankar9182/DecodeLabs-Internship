import pandas as pd

# Load dataset
df = pd.read_excel("Dataset for Data Analytics(1).xlsx")

# Show first 5 rows
print(df.head())

# Check missing values
print(df.isnull().sum())

# Fill missing CouponCode values
df['CouponCode'] = df['CouponCode'].fillna("No Coupon")

# Remove duplicates
df.drop_duplicates(inplace=True)

# Convert Date column into proper format
df['Date'] = pd.to_datetime(df['Date'])

# Clean text columns
df['Product'] = df['Product'].str.strip().str.title()
df['PaymentMethod'] = df['PaymentMethod'].str.strip().str.title()
df['OrderStatus'] = df['OrderStatus'].str.strip().str.title()

# Check duplicate Order IDs
print("Duplicate Order IDs:", df['OrderID'].duplicated().sum())

# Save cleaned dataset
df.to_excel("cleaned_dataset.xlsx", index=False)

print("Data cleaning completed successfully")