# GET zahtev    /rase
# vraca listu rasa
# base url http://javascript.rs
import requests
# http://javascript.rs:5000/rase
odgovor = requests.get("http://javascript.rs:5000/rase").json()
lista_rasa = odgovor["rase"]
print(lista_rasa)

# PRIJAVA
# / prijava
# POST
# body: 
# {"rasa": ____ , "meseci": _____}

ispravno = {"Beba":3, "Stene":10,"Mladi":15,"Odrasli":30}

for rasa in lista_rasa:
    for razred, meseci in ispravno.items():
        adresa = "http://javascript.rs:5000/prijava"
        body = {"rasa":rasa, "meseci": meseci}
        odgovor = requests.post(adresa, json=body).json()
        print(odgovor["razred"]==razred)

# testiranje GET zahteva
# testiranje POST zahteva
# poredjenje rezultata