import requests
from bs4 import BeautifulSoup
# http://gresnik.com/logovanje/logovanje.php
odgovor = requests.get("http://gresnik.com/logovanje/logovanje.php").text
strana = BeautifulSoup(odgovor, "html.parser")
# ispravni kredencijali test 1234
forma = strana.find("form")
akcija = forma["action"]
print(akcija)
konacni_url = "http://gresnik.com/logovanje/" + akcija
podaci = {"username":"test", "password":"1234"}
odgovor_logovanje = requests.post(konacni_url, data=podaci)
print(odgovor_logovanje.status_code)
print(odgovor_logovanje.text)
# 1. ucitati u beautiful soup odgovor_logovanje.text "html.parser"
# 2. locirati h2 element i proveriti da li u njemu pise 
#    Dobrodošli, test korisniče!
ucitana_strana = BeautifulSoup(odgovor_logovanje.text,"html.parser")
ocekivano = "Dobrodošli, test korisniče!"
naslov = ucitana_strana.find("h2").text.strip()
print(ocekivano == naslov)
