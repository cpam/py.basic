import pandas as pd

# Example of Pandas operations
# Package/Method    Description    Syntax and Code Example

# .read_csv() - Reads data from a CSV file and creates a DataFrame.
# Syntax: dataframe_name = pd.read_csv("filename.csv")
# Example:
df = pd.read_csv("data.csv")

# .read_excel() - Reads data from an Excel file and creates a DataFrame.
# Syntax: dataframe_name = pd.read_excel("filename.xlsx")
# Example:
df = pd.read_excel("data.xlsx")

# .to_csv() - Writes DataFrame to a CSV file.
# Syntax: dataframe_name.to_csv("output.csv", index=False)
# Example:
df.to_csv("output.csv", index=False)

# Access Columns - Accesses a specific column using [] in the DataFrame.
# Syntax:
# 1. dataframe_name["column_name"] # Accesses a single column
# 2. dataframe_name[["column1", "column2"]] # Accesses multiple columns
# Example:
age_column = df["age"]
name_and_age_columns = df[["name", "age"]]

# describe() - Generates statistics summary of numeric columns in the DataFrame.
# Syntax: dataframe_name.describe()
# Example:
df_description = df.describe()

# drop() - Removes specified rows or columns from the DataFrame.
# Syntax:
# 1. dataframe_name.drop(["column1", "column2"], axis=1, inplace=True) - Will drop columns
# 2. dataframe_name.drop(index=[row1, row2], axis=0, inplace=True) - Will drop rows
# Example:
df.drop(["age", "salary"], axis=1, inplace=True)  # Will drop columns
df.drop(index=[5, 10], axis=0, inplace=True)  # Will drop rows

# dropna() - Removes rows with missing NaN values from the DataFrame.
# Syntax: dataframe_name.dropna(axis=0, inplace=True)
# Example:
df.dropna(axis=0, inplace=True)

# duplicated() - Identifies duplicate or repetitive values or records within a data set.
# Syntax: dataframe_name.duplicated()
# Example:
duplicate_rows = df[df.duplicated()]

# Filter Rows - Creates a new DataFrame with rows that meet specified conditions.
# Syntax: filtered_df = dataframe_name[(Conditional_statements)]
# Example:
filtered_df = df[(df["age"] > 30) & (df["salary"] < 50000)]

# groupby() - Splits a DataFrame into groups based on specified criteria.
# Syntax:
# 1. grouped = dataframe_name.groupby(by, axis=0, level=None, as_index=True, sort=True, group_keys=True, squeeze=False, observed=False, dropna=True)
# Example:
grouped = df.groupby(["category", "region"]).agg({"sales": "sum"})

# head() - Displays the first n rows of the DataFrame.
# Syntax: dataframe_name.head(n)
# Example:
df_head = df.head(5)

# import pandas as pd - Imports the Pandas library with the alias pd.
# Syntax: import pandas as pd
# Example:
imported_pandas = pd

# info() - Provides information about the DataFrame, including data types and memory usage.
# Syntax: dataframe_name.info()
# Example:
df_info = df.info()

# merge() - Merges two DataFrames based on multiple common columns.
# Syntax: merged_df = pd.merge(df1, df2, on=["column1", "column2"])
# Example:
merged_df = pd.merge(sales, products, on=["product_id", "category_id"])

# print DataFrame - Displays the content of the DataFrame.
# Syntax: print(df) # or just type df
# Example:
print(df)
print(df)

# replace() - Replaces specific values in a column with new values.
# Syntax: dataframe_name["column_name"].replace(old_value, new_value, inplace=True)
# Example:
df["status"].replace("In Progress", "Active", inplace=True)

# tail() - Displays the last n rows of the DataFrame.
# Syntax: dataframe_name.tail(n)
# Example:
df_tail = df.tail(5)
