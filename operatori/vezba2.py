# izracunati porez 20% od cene
cena = int(input("Unesite cenu: "))
porez = 0.2

porez_na_cenu = cena * porez # rezultat programa
# test - unosim 1000, ocekujem da je porez 200
ocekivano = 200.0
dobijeno = porez_na_cenu
print("Test prosao:", ocekivano == dobijeno)
rezultat_testa = ocekivano == dobijeno
print(rezultat_testa)
print(f"Uneli ste cenu: {cena}, porez na cenu: {porez_na_cenu}")