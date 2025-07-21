# scripts/transform.py

import json
import datetime

def transform_data():
    cleaned_data = []

    with open("data/raw_data.json", mode="r", encoding="utf-8") as infile:
        data = json.load(infile)

    for feature in data.get("features", []):
        try:
            props = feature.get("properties", {})
            coords = feature.get("geometry", {}).get("coordinates", [None, None, None])

            earthquake = {
                "Date": datetime.datetime.utcfromtimestamp(props["time"] / 1000).date().isoformat(),
                "Place": props.get("place", "Unknown"),
                "Magnitude": props.get("mag", None),
                "Type": props.get("type", "earthquake"),
                "Longitude": coords[0],
                "Latitude": coords[1],
                "Depth_km": coords[2],
            }

            cleaned_data.append(earthquake)

        except Exception as e:
            print("Skipping record due to error:", e)

    return cleaned_data
