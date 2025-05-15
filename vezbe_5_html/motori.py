import requests
from bs4 import BeautifulSoup

odgovor = requests.get("http://gubitnik.com/vezbe/motori.html").text
strana = BeautifulSoup(odgovor, "html.parser")
lista = strana.find("ul")
stavke = lista.find_all("li") 

ocekivane_vrednosti = ["KTM 890 Duke R","Yamaha MT-07","BMW R1250GS","Honda CB500X"]
dobijene_vrednosti = []
for stavka in stavke:
    dobijene_vrednosti.append(stavka.text.strip())

for model in ocekivane_vrednosti:
    if model in dobijene_vrednosti:
        print("Ok")
    else:
        print(f"Model {model} se ne nalazi u dobijenim vrednostima")


sve_stavke = strana.find_all("li")
for stavka in sve_stavke:
    a_tag = stavka.find("a")
    if a_tag:
        url = "http://gubitnik.com/vezbe/" + a_tag["href"]
        detalji_strana = requests.get(url).text
        detalji_strana_bs = BeautifulSoup(detalji_strana, "html.parser")
        naslov = detalji_strana_bs.find("h1").text
        print(a_tag.text.strip() == naslov.strip())




