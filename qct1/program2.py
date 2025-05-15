import requests
from bs4 import BeautifulSoup

class Proizvod:
    def __init__(self, naziv, cena):
        self.naziv = naziv
        self.cena = cena

odgovor = requests.get("http://javascript.rs/proizvodi.php").text
ocekivani_naslov = "Proizvodi"
strana = BeautifulSoup(odgovor, "html.parser")

dobijeni_naslov = strana.find("h1").text.strip()
print(ocekivani_naslov == dobijeni_naslov)

ocekivani_proizvodi = [
    Proizvod("Pametni Sat", "7990 RSD"), 
    Proizvod("Bluetooth Slušalice", "2990 RSD"), 
    Proizvod("USB Punjač","890 RSD"),
    Proizvod("Bežična Tastatura", "3990 RSD"), 
    Proizvod("Laptop Ranac","3490 RSD"), 
    Proizvod("Gaming Miš", "2490 RSD")
]
ocekivani_zapisi = ["Pametni Sat - 7990 RSD",
"Bluetooth Slušalice - 2990 RSD",
"USB Punjač - 890 RSD",
"Bežična Tastatura - 3990 RSD",
"Laptop Ranac - 3490 RSD",
"Gaming Miš - 2490 RSD"]
lista = strana.find("ul")
stavke = lista.find_all("li") # lista itema

for stavka in stavke:
    if stavka.text.strip() not in ocekivani_zapisi:
        print("Nije u listi")
    else:
        print("U listi je ")

# pronaci prvu li stavku na strani
# uporediti da li u njoj pise Pametni Sat - 7990 RSD
# Koristite stranu za pronalazenje elemenata

ocekivani_naslov = "Pametni Sat - 7990 RSD"
prvi_element = strana.find("li").text.strip()
print(ocekivani_naslov == prvi_element)

prvi_element = strana.find("li")
a_tag = prvi_element.find_next()
print(a_tag["href"] != "")