import pytest
import program1 as pr

class TestJelovnika:
    def test_dodavanje(self):
        jelo = pr.Jelo("Pizza", 300)
        jelo.dodaj_u_porudzbinu()
        assert len(pr.porudzbina) == 1
    
    def test_provera_cene(self):
        jelo = pr.Jelo("Pizza", 300)
        jelo.promeni_cenu_sa_porezom(100) 
        assert jelo.cena == 120
    
    # izracunavanje cene sa porezom
    # ocekivana nova cena da li se poklapa sa 
    # jelo.cena
