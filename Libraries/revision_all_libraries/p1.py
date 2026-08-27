import pandas as pd
import numpy as np

# ==========================================
# 1. LOAD EXCEL FILE
# ==========================================
df = pd.read_excel("data_cleaning_20_records.xlsx")
print(df.head())
print(df.info())

# ==========================================
# 2. CHECK MISSING VALUES
# ==========================================

print(df.isnull().sum())


# ==========================================
# 3. REMOVE EXTRA SPACES
# ==========================================

df["Customer_Name"] = df["Customer_Name"].str.strip()
df["City"] = df["City"].str.strip()
df["Course"] = df["Course"].str.strip()
df["Payment_Status"] = df["Payment_Status"].str.strip()


# ==========================================
# 4. STANDARDIZE TEXT CASE
# ==========================================

df["Customer_Name"] = df["Customer_Name"].str.title()

df["City"] = df["City"].str.title()

df["Course"] = df["Course"].str.title()

df["Payment_Status"] = df["Payment_Status"].str.title()


# ==========================================
# 5. CLEAN CUSTOMER NAME
# Remove special characters
# ==========================================

df["Customer_Name"] = (
    df["Customer_Name"]
    .str.replace(r"[^A-Za-z ]", "", regex=True)
    .str.replace(r"\s+", " ", regex=True)
    .str.strip()
)

#vaibhav patil

# ==========================================
# 6. HANDLE MISSING AGE
# ==========================================

df["Age"] = df["Age"].fillna(df["Age"].median())


# ==========================================
# 7. HANDLE INVALID AGE
# Age should be between 18 and 60
# ==========================================

df.loc[
    (df["Age"] < 18) | (df["Age"] > 60),
    "Age"
] = np.nan

df["Age"] = df["Age"].fillna(df["Age"].median())


# ==========================================
# 8. HANDLE MISSING FEES
# ==========================================

df["Fees"] = df["Fees"].fillna(df["Fees"].median())


# ==========================================
# 9. CLEAN DATE COLUMN
# ==========================================

df["Admission_Date"] = pd.to_datetime(
    df["Admission_Date"],
    errors="coerce",
    dayfirst=False
)

print(df["Admission_Date"])


# ==========================================
# 10. HANDLE INVALID DATES
# ==========================================

print("Invalid Dates:")
print(df[df["Admission_Date"].isna()])


# ==========================================
# 11. CLEAN PHONE NUMBERS
# Remove spaces and hyphens
# ==========================================

df["Phone"] = (
    df["Phone"]
    .astype(str)
    .str.replace(r"[\s-]", "", regex=True)
)


# ==========================================
# 12. VALIDATE PHONE NUMBER
# Indian mobile number = 10 digits
# ==========================================

df["Phone_Valid"] = df["Phone"].str.match(
    r"^[6-9]\d{9}$"
)

print(df[["Phone", "Phone_Valid"]])


# ==========================================
# 13. STANDARDIZE PAYMENT STATUS
# ==========================================

df["Payment_Status"] = (
    df["Payment_Status"]
    .str.strip()
    .str.title()
)

print(df["Payment_Status"].value_counts())


# ==========================================
# 14. CHECK DUPLICATES
# ==========================================

print("Duplicate Records:")

print(df.duplicated().sum())


# ==========================================
# 15. CHECK DUPLICATE CUSTOMER IDs
# ==========================================

print(
    df[df["Customer_ID"].duplicated(keep=False)]
)


# ==========================================
# 16. CREATE AGE GROUP
# ==========================================

df["Age_Group"] = pd.cut(
    df["Age"],
    bins=[0, 25, 35, 45, 100],
    labels=[
        "18-25",
        "26-35",
        "36-45",
        "46+"
    ]
)


# ==========================================
# 17. CREATE FEE CATEGORY
# ==========================================

df["Fee_Category"] = pd.cut(
    df["Fees"],
    bins=[0, 25000, 40000, 60000],
    labels=[
        "Low",
        "Medium",
        "High"
    ]
)


# ==========================================
# 18. REMOVE INVALID PHONE RECORDS
# ==========================================

df = df[df["Phone_Valid"] == True]


# ==========================================
# 19. DROP VALIDATION COLUMN
# ==========================================

df.drop(columns=["Phone_Valid"], inplace=True)


# ==========================================
# 20. RESET INDEX
# ==========================================

df.reset_index(drop=True, inplace=True)


# ==========================================
# 21. FINAL CHECK
# ==========================================

print("\nFinal Data:")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nData Types:")
print(df.dtypes)


# ==========================================
# 22. SAVE CLEAN DATA
# ==========================================

df.to_excel(
    "cleaned_customer_data.xlsx",
    index=False
)

print("Cleaned file saved successfully!")