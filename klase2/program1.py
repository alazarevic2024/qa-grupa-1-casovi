class Kartica:
    # konstruktor - kreira objekat klase
    def __init__(self, tip, stanje, vlasnik, datum_isteka):
        self.tip = tip 
        self.stanje = stanje
        self.vlasnik = vlasnik
        self.datum_isteka = datum_isteka

kartica1 = Kartica("visa", 1000, "jokic", "04/27") 
print(kartica1.tip)
print(kartica1.stanje)

kartica1.vlasnik = "djokovic"
