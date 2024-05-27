import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="temperatures",
    user="postgres",
    password="password"
)

cursor = connection.cursor()
cursor.execute("select * from global_land_temperatures")
records = cursor.fetchall()

for record in records:
    print(record)

cursor.close()
connection.close()