import pandas as pd

# Step 1
path = r"C:\Users\chino\OneDrive\Escritorio\python practices"

# Step 2
df = pd.read_csv(
    path + r"\2. BOMS 2310 2025-12-15 Receta.csv",
    encoding="latin1"
    )

# Step 3
print(df.head())
print(df.shape)
print(df.columns)
print(df.info())

# Step 4
df.columns = df.columns.str.strip()

print(df.columns)

# Step 5
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

print(df.shape)
print(df.columns)

# Step 6
print(df.isnull().sum())

# Step 7
print(df.duplicated().sum())

duplicates = df[df.duplicated()]

print(duplicates.head())

# Step 8
df = df.dropna(axis=1, how='all')

print(df.shape)
print(df.columns)

# Step 9
fg_list = [
    "6971-0009-05",
    "6971-0010-05",
    "6971-0011-02",
    "6971-0012-02",
    "6971-0013-02",
    "6971-0014-02",
    "6971-0015-02",
    "6971-0016-02",
    "6971-0017-02",
    "6971-0018-02",
    "6971-0019-02",
    "6971-0020-02"
]

project_df = df[df["FG P/N"].isin(fg_list)]

print(project_df.shape)
print(project_df["FG P/N"].unique())

# Step 10
column_mapping = {
    "Material": "RawMaterial",
    "Manufactur P/N": "ManufacturPN",
    "L/T": "LeadTime",
    "FG P/N": "FinishedGood"
}

project_df = project_df.rename(columns=column_mapping)

print(project_df.columns)

# Step 11
project_df["RawMaterial"] = project_df["RawMaterial"].str.strip()
project_df["FinishedGood"] = project_df["FinishedGood"].str.strip()

project_df["RawMaterial"] = project_df["RawMaterial"].str.upper()
project_df["FinishedGood"] = project_df["FinishedGood"].str.upper()

print(project_df[["RawMaterial", "FinishedGood"]].head())

print(project_df.columns)

# Step 12
selected_columns = [
    "RawMaterial",
    "Description",
    "Manufactur",
    "ManufacturPN",
    "QPA",
    "Vendor#",
    "Vendor name",
    "LeadTime",
    "Usage",
    "FinishedGood"
]

project_df = project_df[selected_columns]

print(project_df.shape)
print(project_df.columns)
print(project_df.head())

# Step 13
print(project_df.info())
print(project_df.isnull())

# Step 14
print(project_df.dtypes)

project_df["QPA"] = project_df["QPA"].astype(float)
project_df["LeadTime"] = project_df["LeadTime"].astype(int)
project_df["Usage"] = project_df["Usage"].astype(int)

print(project_df.dtypes)

# Step 15
project_df = project_df.sort_values(
    by=["FinishedGood", "RawMaterial"]
)

print(project_df.head())

# Step 16
project_df.to_csv(
    path + r"\clean_bom_project.csv",
    index=False
)

# Step 17
print("Clean BOM exported successfully")