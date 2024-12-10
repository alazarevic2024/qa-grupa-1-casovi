# 1 - nedovoljan, 2 - dovoljan
# 3 - dobar, 4 - vrlo dobar, 5 - odlican
# poslednja opcija - neispravna ocena
ocena = 4 #int(input("Unesite ocenu: "))
if ocena == 5:
    print("Odlican")
elif ocena == 4:
    print("Vrlo dobar")
elif ocena == 3:
    print("Dobar")
elif ocena == 2:
    print("Dovoljan")
elif ocena == 1:
    print("Nedovoljan")
else:
    print("Neispravan unos")