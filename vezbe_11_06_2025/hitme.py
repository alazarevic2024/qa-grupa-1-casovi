# http://gresnik.com/hitme.php
# http://gresnik.com/hitme.php?aim=2
# tekst zadatka http://gresnik.com/vezbe_sa_nitima.txt
import requests
from bs4 import BeautifulSoup
import threading

# funkcija se bavi logovanjem i igrom jednog korisnika i proverom rezultata
def igra(korisnik):
    print(f"Trenutno igra: {korisnik}")
    # logovanje
    sesija = requests.Session()
    odgovor = sesija.post("http://gresnik.com/hitme.php",data={"username":korisnik})
    # korisnik je ulogovan, zapamcena sesija, mozemo dalje
    brojevi = [1, 12, 3, 15, 22]
    for broj in brojevi: # poziva pokusaj za svaki od brojeva - 5 puta
        pokusaj = sesija.get(f"http://gresnik.com/hitme.php?aim={broj}")
        rezultat = pokusaj.text

    # print(rezultat)
    # broj crvenih (promasaj), broj zelenih (pogodak)
    # poklapanje brojeva u rezultatu sa brojem crvenih i zelenih
    strana = BeautifulSoup(rezultat,  features="html.parser")
    svi_divovi = strana.find_all("div")

    broj_pogodaka = 0
    broj_promasaja = 0

    for div in svi_divovi:
        stil = div["style"] # string sa stilizacijom
        # cursor:pointer; float:left;width:40px;height:40px;background-color:yellow;margin:2px;
        if "background-color:red;" in stil:
            broj_promasaja += 1 # crvena boja - broj promasaja uvecavamo
        elif "background-color:green;" in stil:
            broj_pogodaka += 1 # zelena boja - broj pogodaka uvecavamo

    podela = rezultat.split("Rezultat: ")
    # print(podela)
    podela2 = podela[1].split("<br><a href")
    # print(podela2)
    brojevi = podela2[0].split(" / ")
    # print(brojevi)
    # r = rezultat.split("Rezultat: ")[1].split("<br><a href")[0].split(" / ")
    dobijeni_broj_pogodaka = brojevi[0]
    dobijeni_broj_promasaja = brojevi[1]

    print(broj_pogodaka == int(dobijeni_broj_pogodaka))
    print(broj_promasaja == int(dobijeni_broj_promasaja))
    print(f"Zavrsio igrac: {korisnik}")

lista_igraca = ["ana", "marko", "zeljko", "milivoje", "vladimir", "aleksandra"]

niti = []
for korisnik in lista_igraca:
    niti.append(threading.Thread(target=igra, args=[korisnik]))
    # priprema niti
    
for nit in niti:
    nit.start() # startovanje niti

for nit in niti:
    nit.join()
# provera da su sve niti gotove, da bismo kompletirali program

print("Gotovo radno vreme")