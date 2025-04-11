import mysql.connector as conn
# import MySQLdb as conn

konekcija = conn.connect(user="root",passwd="root",port=3306,host="localhost",database="izlozba")
konekcija.autocommit = True

kursor = konekcija.cursor()
kursor.execute("select * from pas")
podaci = kursor.fetchall() # dohvatanje podataka iz upita
print(podaci)
for id,vlasnik,rasa_id,uzrast in podaci:
    print(f"ID:{id}\nVlasnik: {vlasnik}\nID rase: {rasa_id}\nUzrast: {uzrast}\n\n")

    # dobavi rase - koristim izvan funkcije
    # uzmi input od korisnika - koristim izvan funkcije

def unesi_psa(vlasnik,id_rase,uzrast, kursor_t):
    kursor_t.execute(f"insert into pas values (default, '{vlasnik}', {id_rase}, '{uzrast}')")
    # izvrsi upit

kursor.close()
konekcija.close()

if __name__ == "__main__": #izvrsi samo ako te pokrenem iz ovog fajla - kada importujem negde nemoj ovo da izvrsavas
    kursor.execute("select id, naziv from rasa") # sql upit
    rase = kursor.fetchall() # dobavljam podatke
    # Unos psa, ponudjene rase, input podataka
    print("Unesite psa")
    print("Ponudjene rase su:")
    for id,naziv in rase:
        print(f"{id} - {naziv}")

    id_rase = input("Unesite id rase iz liste iznad: ")
    vlasnik = input("Unesite vlasnika: ")
    uzrast = input("Unesite uzrast: ")

    unesi_psa(vlasnik, id_rase, uzrast)