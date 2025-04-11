# program vraca info o proizvodu
# naziv, cenu i opis
'''
 {
    "naziv":"Patike",
    "cena": 100,
    "opis": "Opis proizvoda..."
 }
'''
# proveriti da li se cena uvek vraca kao ceo broj
podaci =  {
    "naziv":"Patike",
    "cena": 100,
    "opis": "Opis proizvoda..."
 }

# lista sa proizvodima
# korisnik unosi zeljeni proizvod
# prikazujemo mu podatke
proizvodi = [
    {"naziv":"patike", "cena": 100, "opis": "Patike nov proizvod"},
    {"naziv": "jakna", "cena": 50, "opis": "Prolecna jakna"},
    {"naziv": "naocare", "cena": 20, "opis": "Naocare za sunce"}
]
pr = input("Unesite naziv proizvoda: ") # unosi neki od naziva

def prikazi_proizvod(pretraga_naziv, podaci):
    for proizvod in podaci:
        if proizvod["naziv"] == pretraga_naziv:
            return proizvod
        
# # pozzivam funkciju - prosledjujem pretragu i podatke za proveru
# print(prikazi_proizvod(pr, proizvodi))

# pripremi podatke za kontekst, dodaj ulazne parametre u pozivu
def testiranje_informacija():
    # kontekst
    probni_podaci = [
    {"naziv":"patike", "cena": 100, "opis": "Patike nov proizvod"},
    {"naziv": "jakna", "cena": 50, "opis": "Prolecna jakna"},
    {"naziv": "naocare", "cena": 20, "opis": "Naocare za sunce"}
    ]
    dobijeni_podaci = prikazi_proizvod("naocare",probni_podaci) # funkcija vraca podatke - nju proveravamo
    ocekivano = probni_podaci[2]
    print(ocekivano == dobijeni_podaci)

testiranje_informacija()