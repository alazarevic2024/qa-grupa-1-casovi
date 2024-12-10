# brzina metka je 10
# skida healtha 20
# na osnovu pozicije 100, treba da ima 5 koraka

# Test nije prosao
# Koraci za reprodukciju buga:
#    Igrac na poziciciji 0, drugi igrac na poziciji 50
#     Brzina je bila 10

# Trenutno stanje:
#     Skinuto je 10 healtha 

# Zeljeno stanje:
#     Za ovo oruzje ocekuje se da skine 20

igrac_1_x = 0
igrac_2_x = 50

jacina = 10
metak = 0
brzina = 10

igrac_2_health = 100
import time
for x in range(5):
    time.sleep(1)
    metak += brzina
    print("Pozicija metka:", metak)
    if metak == igrac_2_x:
        print("Pogodak!!!")
        igrac_2_health -= jacina
        print("Ostalo healtha:", igrac_2_health)

# metak += brzina
# print(metak == igrac_2_x)
# metak += brzina
# print(metak == igrac_2_x)
# metak += brzina
# print(metak == igrac_2_x)
# metak += brzina
# print(metak == igrac_2_x)
# metak += brzina
# print(metak == igrac_2_x)
# #umanji za jacinu udarca
# igrac_2_health -= jacina
# print("Udarac!, trenutni health:", igrac_2_health)
# metak += brzina
# print(metak == igrac_2_x)
# metak += brzina
# print(metak == igrac_2_x)
# metak += brzina
# print(metak == igrac_2_x)
# metak += brzina
# print(metak == igrac_2_x)
# metak += brzina
# print(metak == igrac_2_x)
# #umanji za jacinu udarca
# igrac_2_health -= jacina
# print("Udarac!, trenutni health:", igrac_2_health)

https://collabedit.com/qn4nm