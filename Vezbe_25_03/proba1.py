import mysql.connector

konekcija = mysql.connector.connect(database="sakila", user="root", port=3306, host="localhost",  passwd="root")
kursor = konekcija.cursor()
kursor.execute("select * from actor")
podaci = kursor.fetchall()
print(podaci)