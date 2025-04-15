import mysql.connector as conn
import random

konekcija = conn.connect(database="korisnici",user="root", passwd="root",host="localhost",port=3306)
konekcija.autocommit = True
kursor = konekcija.cursor()

for i in range(30000):
    rand_logovanje = random.randint(100,50000)
    rand_email_number = random.randint(1000,30000)
    kursor.execute(f"insert into korisnik values (default, 'example@{rand_email_number}.com', {rand_logovanje})")