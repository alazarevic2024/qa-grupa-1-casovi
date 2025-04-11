# a - 1
# e - 2
# i - 3
# o - 4
# u - 5
# Rec: ana -> 1n1


# funkcija koja enkriptuje poruku
def enkriptuj_poruku(poruka):
    parovi = {"a":1, "e": 2, "i": 3, "o":4, "u": 5}
    rezultat = ""
    for slovo in poruka: 
        if slovo in parovi: 
            rezultat += str(parovi[slovo]) # parovi["a"]
        else:
            rezultat += slovo # "p" se dodaje u rezultat
    return rezultat # vraca prepakovanu poruku

dobijena_poruka = enkriptuj_poruku("pozdrav")
print(dobijena_poruka)

# [
#     (prosledjeno, ocekivano), #ANA - 1N1 - provera da li ereaguje na velika i mala slova
#     (prosledjeno, ocekivano), #leet code - l22t c4d2
#     (prosledjeno, ocekivano) #qa         - q1
# ]


def test_enkriptuj_poruku():
    # pripremljeni podaci za test slucajeve
    test_podaci = [
        ("ANA", "1N1"),
        ("leet code", "l22t c4d2"),
        ("qa", "q1")
    ]
    # prolazimo kroz test podatke i za svaki pozivamo metod enkriptuj poruku
    # poredimo da li je dobijeni rezultat onaj iz podataka
    for podatak in test_podaci:
        rezultat = enkriptuj_poruku(podatak[0])
        print(rezultat == podatak[1])

# funkcija
# spremni podaci
# funkcija koja testira funkciju


