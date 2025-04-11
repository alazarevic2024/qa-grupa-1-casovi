import mysql.connector as conn

connection = conn.connect(
    host='localhost',
    user='root',
    passwd='root',
    db='sakila', port=3306
)

# Kreiraj kursor
cursor = connection.cursor()

# Izvrši upit
cursor.execute("SELECT * FROM actor")
podaci = cursor.fetchall()
print(podaci)