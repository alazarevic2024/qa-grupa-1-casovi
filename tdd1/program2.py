# kreiraj funkciju saberi - dva pametra a i b
# vraca rezultat sabiranje

def testiraj_sabiranje():
    a = 10
    b = 20
    ocekivano = 30
    dobijeno = sabiranje(a, b)
    print(ocekivano == dobijeno)

def sabiranje(a,b):
    return a+b

testiraj_sabiranje()