import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float

db_path = 'sqlite:///products.db'
engine = create_engine(db_path, echo=True)
metadata = MetaData()

products_table = Table(
    'products', metadata,
    Column('ProductID', Integer, primary_key=True),
    Column('ProductName', String),
    Column('UnitPrice', Float)
)

metadata.create_all(engine)

excel_path = file_path = os.path.join(app.root_path, "PricingReport_20240516_203315894_4588.xlsx"
if not os.path.exists(file_path):
    return jsonify({"error": "Template file not found"}), 404
df = pd.read_excel(excel_path, sheet_name='05-16-2024 Pricing')

df = df.rename(columns={'Product ID': 'ProductID', 'Product Name': 'ProductName', 'Unit Price': 'UnitPrice'})
df.to_sql('products', con=engine, if_exists='replace', index=False)

print("Database setup complete.")
