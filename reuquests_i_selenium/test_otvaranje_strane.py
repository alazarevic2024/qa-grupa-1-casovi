import requests
from bs4 import BeautifulSoup
# http://gubitnik.com/vezbe/motori.html
import pytest

def test_otvaranje_detalja():
    odgovor = requests.get("http://gubitnik.com/vezbe/motori.html").text
    strana = BeautifulSoup(odgovor, "html.parser")
    li_stavka = strana.find("li")
    print(li_stavka.text)
    a_tag = li_stavka.find("a")
    link = a_tag["href"]
    print(link)
    konacni_url = "http://gubitnik.com/vezbe/" + link
    print(konacni_url)
    # Odlazak na novu stranu
    novi_odgovor = requests.get(konacni_url).text
    ocekivani_naslov = li_stavka.text.strip() # ono sto pise na li stavki ocekujem da bude naslov na sledecoj stranici
    nova_strana = BeautifulSoup(novi_odgovor, "html.parser")
    dobijeni_naslov = nova_strana.find("h1").text.strip()
    assert dobijeni_naslov == ocekivani_naslov

pytest.main()