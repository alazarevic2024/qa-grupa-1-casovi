import unittest
import program1 as pr

class JelovnikTestiranje(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("######## IZVRSAVAM SE NA POCETKU ############")
    @classmethod
    def tearDownClass(cls):
        print("######### IZVRSAVAM SE NA KRAJU #############")

    def setUp(self):
        print("IZVRSAVAM PRE SVAKOG TESTA")
        pr.porudzbina.clear()
    
    def tearDown(self):
        print("** IZVRSAVAM NAKON SVAKOG TESTA **")

    def test_provera_cene(self):
        print("TEST 1")
        cena = 100 #nova cena
        ocekivana_cena_sa_porezom = 120 # ocekivana nova cena sa porezom
        jelo = pr.Jelo("Pizza", 1000)
        jelo.promeni_cenu_sa_porezom(cena)
        self.assertEqual(ocekivana_cena_sa_porezom, jelo.cena)

    def test_provera_dodavanja_a(self):
        print("TEST 2")
        jelo = pr.Jelo("",0)
        jelo.dodaj_u_porudzbinu()
        self.assertIn(jelo, pr.porudzbina)
        self.assertEqual(len(pr.porudzbina), 1)

    def test_provera_dodavanja_b(self):
        print("TEST 3")
        jelo = pr.Jelo("Gulas", 100)
        jelo.dodaj_u_porudzbinu()
        self.assertIn(jelo, pr.porudzbina)
        self.assertEqual(len(pr.porudzbina), 1)
        

# unittest.main()
grupa = unittest.TestSuite()
grupa.addTest(JelovnikTestiranje("test_provera_dodavanja_b")) # testiram samo poslednju
grupa.addTest(JelovnikTestiranje("test_provera_dodavanja_a"))
runner = unittest.TextTestRunner()
runner.run(grupa)