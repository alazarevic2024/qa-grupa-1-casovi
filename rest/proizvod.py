import requests

# vraca informacije o proizvodu
# testirati informacije
# GET
adresa = "http://gresnik.com/proizvod.php"

odgovor = requests.get(adresa).json()
print(odgovor)
# print(odgovor["naziv"])
# print(odgovor["cena"])
# print(odgovor["kategorija"])
ocekivani_naziv = "Hleb"
ocekivana_cena = 60
ocekivana_kategorija = "Pekara"
assert ocekivani_naziv == odgovor["naziv_proizvoda"]
assert ocekivana_cena == odgovor["cena_proizvoda"]
assert ocekivana_kategorija == odgovor["kategorijaProizvoda"]