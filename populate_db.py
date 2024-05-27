import csv
import os
import psycopg2

def read_csv_and_insert_to_db(relative_path, delimiter):
    script_dir = os.getcwd()
    abs_file_path = os.path.join(script_dir, relative_path)

    print(f"Current directory: {os.getcwd()}")
    print(f"Absolute file path: {abs_file_path}")

    # Verifica si el archivo existe
    if not os.path.exists(abs_file_path):
        print(f"Error: The file '{abs_file_path}' was not found.")
        return

    # Conectar a la base de datos PostgreSQL
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="temperatures",
            user="postgres",
            password="password"
        )
        cursor = connection.cursor()
        print("Connected to the database.")
        
        # Leer el contenido del archivo CSV e insertar los datos en la base de datos
        with open(abs_file_path, 'r') as csv_f:
            rows = csv.reader(csv_f, delimiter=delimiter)
            next(rows)  # Omitir el encabezado
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
        # Cerrar cursor y conexión
        if cursor:
            cursor.close()
        if connection:
            connection.close()
        print("Database connection closed.")

# Ruta relativa del archivo CSV
relative_path = 'data/globalLandTemperaturesByCountry.csv'
read_csv_and_insert_to_db(relative_path, ',')
