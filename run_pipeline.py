# main.py

from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.load import load_data

print("🔁 Starting Earthquake Data ETL Pipeline...")

extract_data()
print("✅ Data extracted from USGS API.")

data = transform_data()
print(f"✅ Transformed {len(data)} earthquake records.")

load_data(data)
print("🎉 All earthquake data loaded to PostgreSQL.")
