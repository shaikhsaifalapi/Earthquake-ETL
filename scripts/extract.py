# scripts/extract.py

import requests
import json
import os
from datetime import datetime, timedelta

def extract_data():
    # Fetch earthquakes in the past 30 days
    base_url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
    params = {
        "format": "geojson",
        "starttime": (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d"),
        "endtime": datetime.now().strftime("%Y-%m-%d"),
        "minmagnitude": 4.5
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    os.makedirs("data", exist_ok=True)

    with open("data/raw_data.json", mode="w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)

    print("✅ Earthquake data extracted and saved to data/raw_data.json")
