import csv
import os
import psycopg2
import time

def connect_to_db():
    retries = 5
    while retries > 0:
        try:
            connection = psycopg2.connect(
                host=os.getenv('DB_HOST'),
                database=os.getenv('DB_NAME'),
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASS')
            )
            return connection
        except psycopg2.OperationalError as e:
            print(f"Error: {e}")
            print(f"Retrying in 5 seconds... ({retries} retries left)")
            retries -= 1
            time.sleep(5)
    raise Exception("Could not connect to the database after multiple attempts")

def read_csv_and_insert_to_db(relative_path, delimiter):
    script_dir = os.getcwd()
    abs_file_path = os.path.join(script_dir, relative_path)

    print(f"Current directory: {os.getcwd()}")
    print(f"Absolute file path: {abs_file_path}")

    if not os.path.exists(abs_file_path):
        print(f"Error: The file '{abs_file_path}' was not found.")
        return

    connection = None
    cursor = None

    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        print("Connected to the database.")

        with open(abs_file_path, 'r') as csv_f:
            rows = csv.reader(csv_f, delimiter=delimiter)
            next(rows)  # Skip header
            for r in rows:
                country, year, temperature = r[0], r[1], r[2]
                insert_query = """
                INSERT INTO global_land_temperatures (country, year, temperature)
                VALUES (%s, %s, %s);
                """
                print(country, year, temperature)
                cursor.execute(insert_query, (country, year, temperature))
            connection.commit()
            print("Data inserted successfully.")

    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
        print("Database connection closed.")

if __name__ == "__main__":
    relative_path = os.getenv('DATA_FILE', 'globalLandTemperaturesByCountry.csv')
    read_csv_and_insert_to_db(relative_path, ',')
