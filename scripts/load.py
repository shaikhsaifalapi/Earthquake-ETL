# scripts/load.py

import psycopg2

def load_data(data):
    # 🔐 PostgreSQL credentials — change as needed
    DB_HOST = "localhost"
    DB_PORT = "5432"
    DB_NAME = "earthquake_data"
    DB_USER = "postgres"
    DB_PASSWORD = "root"  # Replace with your real password

    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )

        cursor = conn.cursor()

        # Create table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS earthquake_data (
                Date DATE,
                Place TEXT,
                Magnitude REAL,
                Type TEXT,
                Longitude REAL,
                Latitude REAL,
                Depth_km REAL
            )
        """)

        # Optional: clear old data
        cursor.execute("DELETE FROM earthquake_data")

        # Insert each row
        for row in data:
            cursor.execute("""
                INSERT INTO earthquake_data (Date, Place, Magnitude, Type, Longitude, Latitude, Depth_km)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (
                row["Date"],
                row["Place"],
                row["Magnitude"],
                row["Type"],
                row["Longitude"],
                row["Latitude"],
                row["Depth_km"]
            ))

        conn.commit()
        print("✅ Earthquake data loaded into PostgreSQL.")

    except Exception as e:
        print("❌ Error loading to PostgreSQL:", e)

    finally:
        if conn:
            cursor.close()
            conn.close()
