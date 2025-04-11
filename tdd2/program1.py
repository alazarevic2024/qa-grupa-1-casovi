# naziv, cena
class Jelo:
    def __init__(self, naziv, cena):
        self.naziv = naziv
        self.cena = cena
    
    def ispisi_informacije(self):
        print(f"Informacije o jelu:\nNaziv: {self.naziv}....Cena: {self.cena}")
    # dodajemo novu cenu i uracunavamo porez 20%
    def promeni_cenu_sa_porezom(self, nova_cena):
        self.cena = nova_cena + (nova_cena * 0.2)

    def dodaj_u_porudzbinu(self):
        porudzbina.append(self)

porudzbina = []

if __name__ == "__main__":
    jelo_1 = Jelo("Cevapi", 300)
    print(jelo_1.naziv)
    jelo_1.ispisi_informacije()
    jelo_1.promeni_cenu_sa_porezom(500)
    print(jelo_1.cena)
    jelo_1.ispisi_informacije()

