godine = 15
minimum = 13
                   # True / False
print("Uspesno:", godine >= minimum)
    # provera
if godine >= minimum:
    print("Uspesno!")
    print("Ispunili ste uslove!")

print("nastavak programa...")
#-----------------------------------
# Ispisati welcome ako su tacni i kor ime i sifra
kor_ime = "admin"
sifra = "123"
sacuvano_ime = "admin"
sacuvana_sifra = "1234"

if kor_ime == sacuvano_ime or sifra == sacuvana_sifra:
    print("Welcome!")

# Ispisi "Broj je paran", ako je deljiv sa 2
# % , ostatak pri deljenju jednak nuli
# rezultat ostatka pri deljenju sa 2
# provera da li je razultat jednak 0
# ako je provera uspesna ispisuje poruku
broj = 7
ostatak_pri_deljenju = broj % 2 # 0 ili neki drugi broj
provera = broj % 2 == 0 # True ili False
if broj % 2 == 0:
    print("Broj je paran")

# Ispisati da li je broj pozitivan - "Broj je pozitivan"
# provera da li je veci od 0
broj = 10
if broj > 0:
    print("Broj je pozitivan")
#        x    cilj
# Ispisati stigao samo ako je pozicija jednaka odredistu
# Ispisati poruku ako je prosao odrediste
automobil_pozicija = 0
odrediste = 10

automobil_pozicija += 2
automobil_pozicija += 2
automobil_pozicija += 2
automobil_pozicija += 2
automobil_pozicija += 2
automobil_pozicija += 2

if automobil_pozicija > odrediste:
    print("Prosli ste odrediste.")


# Omoguciti korisniku da kupi nesto samo ako je ulogovan
# nakon provere o logovanju, vrsiti dalje provere - cene, da li ima dovoljno novca
# a ako nije ulogovan, ne raditi dalje nista

ulogovan = True
novac_na_racunu = 100
cena_proizvoda = 50

if ulogovan:
    print("Korisnik je ulogovan, moze dalje.")
    print("Prikaz proizvoda - ubacite proizvode u korpu")
    print("Korisnik u korpi")
    if novac_na_racunu >= cena_proizvoda:
        print("Uspesna kupovina, imate dovoljno novca na racunu.")
        print("Prikazi uspesnu transakciju")
    print("Prikazi filtere")

print("U svakom slucaju i da je ulogovan i da nije ulogovan...")

# Proveriti brzinu samo ako je auto u pokretu
brzina_automobila = 100
ogranicenje = 80
vec_urucena_kazna = False
if brzina_automobila > 0:
    print("Auto je u pokretu")
    if brzina_automobila > ogranicenje:
        print("Prekoracena brzina")
        if vec_urucena_kazna:
            print("Oduzeti vozilo.")

novac_na_racunu = 100
cena = 50
naziv_proizvoda = "Patike"
# Komanda 1 - prikazuje info o proizvodu Naziv: ....   Cena: ... $
# Komanda 2 - kupuje # ispisati novo stanje nakon kupovine
# Komanda 3 - Izlazi
komanda = int(input("Unesite komandu: "))
if komanda == 1:
    print(f"Naziv: {naziv_proizvoda}\tcena: {cena}$")
if komanda == 2:
    if novac_na_racunu >= cena:
        novac_na_racunu -= cena
        print(f"Uspesno ste kupili, novo stanje: {novac_na_racunu}")
if komanda == 3:
    print("Hvala na poseti.")















