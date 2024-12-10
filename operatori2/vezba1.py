godine = 10
minimum_za_pristup = 13
print("Dozvoljen pristup:",godine >= minimum_za_pristup)

stanje_na_racunu = 1000
cena_proizvoda = 800
print("Uspesna kupovina:", stanje_na_racunu >= cena_proizvoda)

# broj = int(input("Unesite broj: "))
# # % ostatak pri deljenju
# # paran broj pri deljenju sa 2 ima ostatak 0

# rezultat = (broj % 2) == 0
# print("Broj je paran:", rezultat)
# import random

# unet_broj = int(input("Unesite broj od 1 do 10: "))
# racunar = random.randint(1,10)
# print(f"Uneti broj: {unet_broj}\tRacunar: {racunar}")
# print("Hit:", unet_broj == racunar)

kor_ime = "admin"
sifra = "123"
uneto_ime = "admin"
uneta_sifra = "1234"

print(kor_ime == uneto_ime)
print(sifra == uneta_sifra)

provera_ime = kor_ime == uneto_ime
provera_sifra = sifra == uneta_sifra
print(provera_ime and provera_sifra)
print(kor_ime == uneto_ime and sifra == uneta_sifra)
# print(False and True)

obavezno_logovanje = True
minimalne_godine = 13
# -------------------------
ulogovan = False
godine = 15
print("Prikazi sadrzaj:", obavezno_logovanje == ulogovan and minimalne_godine <= godine)
# --------------------------
# kriterijumi za kupovinu
maksimalni_iznos = 5000
ima_garanciju = True
# ----------------------
# pronadjeni proizvod
cena = 4000
garancija = True

print("Kupujem: ", maksimalni_iznos >= cena and ima_garanciju == garancija)

# registrujte se: unesite ili email ili broj tel - bar jedno
# Uspesno: True/False - ako bar jedno nije prazno - ovo je prazno ""
uneti_email = ""
uneti_telefon = ""
print("Uspesno:", uneti_email != "" or uneti_telefon != "")

# dovoljno novca, da je prozivod dostupan, da je ulogovan ili gost
# nasi podaci u sistemu
novac_na_racunu = 1000
cena = 800
ulogovan = True
gost = False
dostupan = True

print(novac_na_racunu >= cena and dostupan == True and (ulogovan or gost))
# and, or, not
# not    False -> True     True - > False

ukljucen_zvuk = True
print("Zvuk ukljucen:", ukljucen_zvuk)
ukljucen_zvuk = not ukljucen_zvuk

print("Zvuk ukljucen: ", ukljucen_zvuk)

godine = 15
print(not(godine > 18))
# not - ispred bilo koje bool vrednosti True / False

korisnik = bin(1)
print(korisnik)
admin = bin(4)
print(admin)
superadmin = bin(2)
print(superadmin)









