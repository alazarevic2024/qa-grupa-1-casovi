#              0, 1, 2, 3, 4
        # pocetak, kraj, korak
for x in range(1, 5, 2):
    print(x)

pocetna_godina = 2010
krajnja_godina = 2020

# for godina in range(pocetna_godina, krajnja_godina + 1):
#     print(godina, end="*")

proizvod = "Telefon"
cena = 100
print(f"Proizvod: {proizvod}", end=" ")
print(f"Cena: {cena}")
print("Kraj programa")

print(proizvod, end= "\t")
print(cena)
# 0                 20
# X                cilj
automobil_pozicija = 0
pocetak = 0
cilj = 20
for put in range(pocetak, cilj + 1):
    print(f"Automobil pozicija: {automobil_pozicija}")
    if automobil_pozicija == cilj:
        print("stigao")
    automobil_pozicija += 1
