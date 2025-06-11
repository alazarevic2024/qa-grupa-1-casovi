import requests
from bs4 import BeautifulSoup
import random

session = requests.Session()

podaci = {"username":"dovla","password":"123"}
odgovor = session.post("http://gresnik.com/sabiranje.php", data=podaci)
print(odgovor.text)
sesija = odgovor.headers["Set-Cookie"] # korisnicka sesija

a = random.randint(1, 100)
b = random.randint(1, 100)
podaci_sabiranje = {"a":f"{a}", "b": f"{b}", "saberi": "+"}
odgovor_sabiranja = session.post("http://gresnik.com/sabiranje.php", data= podaci_sabiranje) #, headers={"Cookie":sesija}
print(odgovor_sabiranja.text)

strana = BeautifulSoup(odgovor_sabiranja.text, features="html.parser")
rezultat = strana.find("span").text.strip()
print(rezultat)
ocekivano = f"{a} + {b} = {a+b}"

print(ocekivano == rezultat)