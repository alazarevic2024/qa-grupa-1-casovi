# prezime = "Jokic"
# tim = "Denver"
# broj = 15
# energija = 100
#       podaci[0]    podaci[1]     podaci[2]
# podaci = [prezime,      tim,         broj]
# podaci_recnik = {"prezime":prezime, "tim":tim, "broj":broj}
# #       podaci_recnik["prezime"]   
   
class Igrac:
    prezime     = ""    # polje, svojstvo, atribut, property
    tim         = ""
    broj        = 0
    energija    = 0

igrac1 = Igrac()
igrac1.prezime = "Jokic"
igrac1.broj = 15
igrac1.tim = "Denver"
igrac1.energija = 100
print(igrac1.prezime, igrac1.broj, igrac1.tim, igrac1.energija)

igrac2 = Igrac()
igrac2.broj = 77
igrac2.tim = "Lakers"
igrac2.energija = 90
igrac2.prezime = "Doncic"

igrac2.energija -= 10

print(igrac2.energija)

novi_tim = [igrac1, igrac2]

for igrac in novi_tim:
    print(igrac.prezime)