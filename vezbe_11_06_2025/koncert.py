# http://gresnik.com/koncert.php
# tekst zadatka http://gresnik.com/koncert.txt
import requests
from bs4 import BeautifulSoup

ime = "aleksandra"
sesija = requests.Session()
odgovor = sesija.post("http://gresnik.com/koncert.php", data={"ime": ime})
print(odgovor.text)

strana = BeautifulSoup(odgovor.text, "html.parser")
dobijeno_ime = strana.find("p")
print(dobijeno_ime.text)
print(dobijeno_ime.text == f"Zdravo, {ime}")#ocekivano - dobijeno

opcije = strana.find_all("option")
print(opcije)
lista_opcija = []
for opcija in opcije:
    lista_opcija.append(opcija["value"])
print(lista_opcija)

for o in lista_opcija:
    glasanje_odgovor = sesija.post("http://gresnik.com/koncert.php", data={"bend":o})
    print(glasanje_odgovor.text)