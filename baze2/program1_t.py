import mysql.connector as conn
# import MySQLdb as conn
import unittest
import program1

class IzlozbaTestiranje(unittest.TestCase):
    def setUp(self):
        self.konekcija = conn.connect(user="root",passwd="root",port=3306,host="localhost",database="izlozba")
        self.konekcija.autocommit = True
        self.kursor = self.konekcija.cursor()

    def test_unos_psa(self):
        # priprema podataka
        vlasnik = "Petar"
        rasa_id = 10
        uzrast = "mladi"
        # unos
        program1.unesi_psa(vlasnik,rasa_id, uzrast, self.kursor)
        # provera unosa
        # proveri da li je poslednji red jednak unetom
        self.kursor.execute("select * from pas order by id desc limit 1")
        rezultat = self.kursor.fetchone()
        self.assertEqual(rezultat[1],vlasnik)
        self.assertEqual(rezultat[2],rasa_id)
        self.assertEqual(rezultat[3],uzrast)

unittest.main()