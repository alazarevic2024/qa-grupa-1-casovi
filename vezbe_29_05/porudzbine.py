# http://javascript.rs:5000/porudzbine
import requests
# http://javascript.rs/dokumentacija1.html
# Bice na portu 5000

base_url = "http://javascript.rs:5000"

# test get zahteva za dobijanje porudzbina
def test_porudzbine():
    url = base_url + "/porudzbine"
    odgovor = requests.get(url).json()
    print(odgovor)
    return len(odgovor)

print(test_porudzbine())

def test_dodaj_porudzbinu():
    trenutni_broj = test_porudzbine() # broj pre dodavanja
    url = base_url + "/poruci"
    body = {
        "naziv":"Nova pizza",
        "ime": "Gost",
        "velicina":"srednja",
        "dodaci":[]
    }
    odgovor = requests.post(url,json=body).json()
    dobijeno = odgovor["poruka"]
    print(dobijeno == "Porudžbina dodata.")
    novi_broj = test_porudzbine()
    print(trenutni_broj+1 == novi_broj)

test_dodaj_porudzbinu()

def test_brisanje(id):
    url = base_url + f"/poruci/{id}"
    odgovor = requests.delete(url).json()
    obrisano = odgovor["obrisano"]
    obrisan_id = obrisano["id"]
    print(obrisan_id == id) # da li je obrisan id koji smo prosledili

test_brisanje(13)