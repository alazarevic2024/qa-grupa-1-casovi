class Bend: 
    naziv = ""
    satnica = ""

    def __init__(self, naziv, satnica):
        self.naziv = naziv
        self.satnica = satnica
    
    def izracunaj(self, trajanje):
        return self.satnica * trajanje
        
    # metoda
    def predstavi_bend(self):
        pass

def test_izracunaj():
    bend = Bend("nicim izazvan", 300)
    trajanje = 3
    ocekivano = 900
    dobijeno = bend.izracunaj(trajanje)
    print(ocekivano == dobijeno)

# funkcija
def pozdrav():
    pass

bend = Bend("Nicim izazvan", 100)