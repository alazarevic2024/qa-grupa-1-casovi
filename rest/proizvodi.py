import requests

odgovor = requests.get("http://gresnik.com/proizvodi.php").json()
print(odgovor)
# Naziv: ///
# Cena: ///
############
lista_proizvoda = odgovor["proizvodi"]
print(lista_proizvoda)

# for proizvod in lista_proizvoda:
#     print(f"Naziv: {proizvod["naziv"]}\nCena: {proizvod["cena"]}\n########")

for proizvod in lista_proizvoda:
    print("naziv"in proizvod)
    print("cena"in proizvod)