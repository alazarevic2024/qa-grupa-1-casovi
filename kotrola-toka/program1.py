broj = 9

if broj % 2 == 0:
    print("Paran broj")
else:
    print("Broj nije paran")

print("Izvrsava se u svakom slucaju")

komanda = int(input("Unesite komandu"))
naziv = "Patike"
cena = 100
nova_cena = 100
if komanda == 1:
    print(f"Naziv: {naziv}, cena: {nova_cena}")
if komanda == 2: 
    if cena > nova_cena:
        print(f"Proizvod je snizen za {cena - nova_cena}")
    else:
        print("Proizvod nije na snizenju.")



