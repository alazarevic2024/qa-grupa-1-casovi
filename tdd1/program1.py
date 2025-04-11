def saberi(a,b):
    return a-b

def testiraj_sabiranje():
    # podaci
    a = 10
    b = 15
    # poziv funkcije
    dobijeno = saberi(a, b)
    ocekivano = 25
    print(f"Funkcija - sabiranje -Test je: {dobijeno == ocekivano}\n ocekivano: {ocekivano} - dobijeno: {dobijeno}")


rezultat = saberi(5, 9)
print(rezultat)

testiraj_sabiranje()