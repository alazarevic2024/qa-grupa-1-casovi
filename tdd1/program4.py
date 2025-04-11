# Prijavi psa na izlozbu
# Ime (string), broj meseci (int), rasa (string)
# Odrediti grupu prema broju meseci - funkcionalnost
# Upisi psa u evidenciju - funkcionalnost

# 3-6 - bebe, 6 - 9 -najmladji, 9 - 18 mladi, 18 > zreli, > 96 veterani

def test_odredi_grupu_bebe():
    opseg = range(3, 7) # [3, 4, 5, 6]
    ocekivano = "bebe"
    for broj_meseci in opseg:
        dobijeno = odredi_grupu(broj_meseci)
        print(f"TC - Bebe grupa: meseci: {broj_meseci}", ocekivano == dobijeno)

def test_odredi_grupu_najmladji():
    opseg = range(7, 10) # [7, 8 ]
    ocekivano = "najmladji"
    for broj_meseci in opseg:
        dobijeno = odredi_grupu(broj_meseci)
        print(f"TC - Najmladji grupa: meseci: {broj_meseci}", ocekivano == dobijeno)

def test_odredi_grupu_mladi():
    broj_meseci = 15
    ocekivano = "mladi"
    dobijeno = odredi_grupu(broj_meseci)
    print("TC - Mladi grupa: ", ocekivano == dobijeno)

def test_odredi_grupu_zreli():
    broj_meseci = 20
    ocekivano = "zreli"
    dobijeno = odredi_grupu(broj_meseci)
    print("TC - Zreli grupa: ", ocekivano == dobijeno)

def test_odredi_grupu_veterani():
    broj_meseci = 96
    ocekivano = "veterani"
    dobijeno = odredi_grupu(broj_meseci)
    print("TC - Veterani grupa: ", ocekivano == dobijeno)

def test_odredi_grupu_neispravan_unos():
    ocekivano = "neispravan unos"
    opseg_manje_od_3 = [-5, -2, 0, 1, 2]
    opseg_vece_od_365 = range(366,400)
    opseg = opseg_manje_od_3 + list(opseg_vece_od_365)
    for broj_meseci in opseg:
        dobijeno = odredi_grupu(broj_meseci)
        print(f"TC - Neispravan unos: {broj_meseci} ", ocekivano == dobijeno)  

def odredi_grupu(meseci):
    if meseci >= 3 and meseci <= 6:
        return "bebe"
    elif 6 < meseci <= 9:
        return "najmladji"
    elif meseci > 9 and meseci < 18:
        return "mladi"
    elif meseci >= 18 and meseci < 96:
        return "zreli"
    elif meseci >= 96 and meseci < 360:
        return "veterani"
    else:
        return "neispravan unos"

test_run = [test_odredi_grupu_bebe, test_odredi_grupu_najmladji, test_odredi_grupu_mladi, test_odredi_grupu_neispravan_unos]
for test_slucaj in test_run:
    test_slucaj()