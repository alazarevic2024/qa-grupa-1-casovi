import requests

odgovor = requests.get("http://gresnik.com/api.php").json()

for clanak in odgovor:
    naslov = clanak["naslov"] #naslov iz liste svih clanaka
    id_clanka = clanak["idclanka"]
    odgovor = requests.get(f"http://gresnik.com/api.php?id={id_clanka}").json()
    print(odgovor)
    detalji_naslov = odgovor["naslov"] #naslov iz detalja
    # provera da li se poklapaju
    assert naslov == detalji_naslov