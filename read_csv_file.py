import csv
import os

def read_csv(relative_path, delimiter):
    script_dir = os.getcwd()  
    abs_file_path = os.path.join(script_dir, relative_path)

    print(f"Current directory: {os.getcwd()}")
    print(f"Absolute file path: {abs_file_path}")

    # Verifica si el archivo existe
    if not os.path.exists(abs_file_path):
        print(f"Error: The file '{abs_file_path}' was not found.")
        return

    # Lee y muestra el contenido del archivo CSV
    with open(abs_file_path, 'r') as csv_f:
        cnt = -1
        rows = csv.reader(csv_f, delimiter=delimiter)
        for r in rows:
            if cnt == -1:
                print(f'{" | ".join(r)}')
            else:
                print(f'{r[0]} | {r[1]} | {r[2]} | {r[3]}')
            cnt += 1


relative_path = 'data/globalLandTemperaturesByCountry.csv'
read_csv(relative_path, ',')