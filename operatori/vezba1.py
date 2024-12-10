temperatura = 2
grad = "Novi Sad"
opis = "Sneg"

# Trenutna temperatura: 1 stepen
# Grad: Beograd
# Trenutno je: sneg  - wrap teksta alt z
print("Trenutna temperatura:",temperatura, "\n", "stepen", "\n")
print(f"Trenutna temperatura: {temperatura} stepen\nGrad: {grad}\nTrenutno je: {opis}")

ispis = "Trenutna temperatura: " + str(temperatura)
print(ispis)
opis_progonoze = "Trenutno je: " + opis
print(opis_progonoze)
print(ispis + "\n" + opis_progonoze) #konkatenacija stringova

# unesite prvi broj, drugi broj, ispis rezultata
broj1 = 20 #input("Unesite prvi broj: ")
broj2 = 50 #input("Unesite drugi broj: ")
rezultat = int(broj1) + int(broj2) # + - * / aritmeticki
ocekivano = 60
# == operator poredjenja - jednakosti
print(rezultat == ocekivano)
print(f"Rezultat je: {rezultat}")

print(10 / 2)
#deljenje bez ostatka
print(10 // 2)
print(9 // 2)
print(2 ** 8) # stepenovanje, posle ** je stepen
# celobrojni ostatak pri deljenju
print(10 % 3) # 3*3 + 1
print(10 % 2)

# r na kvadrat pi - povrsina kruga 
poluprecnik = 5
pi = 3.14
# povrsina = poluprecnik * poluprecnik * pi
povrsina = poluprecnik ** 2 * pi
print(povrsina)
# testiramo
ocekivano = 78.5
dobijeno = povrsina

print(-ocekivano)
ocekivano = -ocekivano
print(ocekivano == dobijeno)

auto_x = 0
parking_x = 40

# auto_x += parking_x # odmah je stigao
print(auto_x)
# pomera za 10
auto_x += 10
print(auto_x)
auto_x += 10
print(auto_x)
auto_x += 10
print(auto_x)
auto_x += 10
print(auto_x)
# proveriti da li je auto na poziciji parkinga
print("Stigao", auto_x == parking_x)
auto_x -= 5
print("Stigao", auto_x == parking_x)

auto_x *= 2
print(auto_x)
