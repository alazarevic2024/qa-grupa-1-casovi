#   sr,     de,   en
# Zdravo, Hallo, Hello
# odabran_jezik = input("Odaberite jezik (sr, de, en): ")
odabran_jezik_test_vrednost = "sr"
odabran_jezik = odabran_jezik_test_vrednost
prevod = "" # dobijeno
ocekivani_prevod = "Zdravo" # ocekivano
if odabran_jezik == "sr":
    prevod = "Zdravo"
elif odabran_jezik == "en":
    prevod ="Hello"
elif odabran_jezik == "de":
    prevod = "Hallo"
else:
    prevod = "Prevod nije podrzan"

if prevod == ocekivani_prevod:
    print("Test je prosao")
else: 
    print(f"Test nije prosao, proverite prevod za: {odabran_jezik}")