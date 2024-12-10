# + - * /
broj1 = int(input("Unesite prvi broj: "))
operacija = input("Unesite operaciju (+, -, *, /): ")
broj2 = int(input("Unesite drugi broj: "))
rezultat = 0

if operacija == "+":
    rezultat = broj1 + broj2
elif operacija == "-":
    rezultat = broj1 - broj2
elif operacija == "*":
    rezultat = broj1 * broj2
elif operacija == "/":
    rezultat = broj1 / broj2
else:
    print("Operacija nije podrzana")

