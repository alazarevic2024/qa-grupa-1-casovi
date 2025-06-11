import requests
import threading
session = requests.Session()

korisnici = {"dovla":"123", "aleksandra":"234", "loshmi":"456"}

def logovanje(username, password):
    podaci = {"username":username,"password":password}
    odgovor = session.post("http://gresnik.com/sabiranje.php", data=podaci)
    print(f"Loguje se: {username}")

# simulacija 100 korisnika (random)
for x in range(100):
    nit = threading.Thread(target=logovanje, args=[f"korisnik {x}", "123"])
    nit.start()

# simulacija korisnika
for username, password in korisnici.items():
    nit = threading.Thread(target=logovanje, args=[username, password])
    nit.start()

