# update_database.py
import pandas as pd
from sqlalchemy import create_engine

# Database connection
db_path = 'sqlite:///products.db'
engine = create_engine(db_path, echo=True)

# Load data from new Excel file
new_excel_path = '/path/to/new/excel/file.xlsx'
df = pd.read_excel(new_excel_path, sheet_name='05-16-2024 Pricing')

# Update data in the database
df = df.rename(columns={'Product ID': 'ProductID', 'Product Name': 'ProductName', 'Unit Price': 'UnitPrice'})
df.to_sql('products', con=engine, if_exists='replace', index=False)

print("Database update complete.")
