from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
import time
import pytest
import os
# TC-1 - Login sa ispravnim podacima         TC -2 - Login bez unetih podataka
# Dolazak na grenik.com                      Dolazak na gresnik.com      
# Klik na taster Login                       Klik na taster Login
# Unos ispravnih podataka                    Ostavljena prazna polja za kor ime i sifru
# Klik na login                              Klik na login
# Ocekivano: uspesno ulogovan korisnik       Ocekivano: neuspesan login

# TC - 3 - Login sa neispravnim podacima
# -----------------------------------------------------------------
# TC 1 - login sa ispravnim podacima
# def test_ispravan_login():
#     browser = Firefox()
#     browser.get("http://gresnik.com")
#     browser.find_element(By.LINK_TEXT, "Log in").click()
#     time.sleep(2)
#     browser.find_element(By.NAME, "user").send_keys("Autor")
#     browser.find_element(By.NAME, "pass").send_keys("123")
#     browser.find_element(By.NAME, "submit").click()
#     time.sleep(3)
#     naslov = browser.find_element(By.XPATH, "//h3[text()='Admin panel']")
#     assert naslov.text.strip() == "Admin panel"

# # TC 2 - login bez unetih podataka - ocekivano: ostajem na login strani
# def test_prazni_podaci_login():
#     browser = Firefox()
#     browser.get("http://gresnik.com")
#     browser.find_element(By.LINK_TEXT, "Log in").click()
#     time.sleep(2)
#     browser.find_element(By.NAME, "user").send_keys("")
#     browser.find_element(By.NAME, "pass").send_keys("")
#     browser.find_element(By.NAME, "submit").click()
#     time.sleep(3)
#     naslov = browser.find_element(By.XPATH, "//h3[text()='Log in']")
#     assert naslov.text.strip() == "Log in"
    
# # TC 3 - login sa neispravnim podacima
# def test_neispravan_login():
#     browser = Firefox()
#     browser.get("http://gresnik.com")
#     browser.find_element(By.LINK_TEXT, "Log in").click()
#     time.sleep(2)
#     browser.find_element(By.NAME, "user").send_keys("Proba")
#     browser.find_element(By.NAME, "pass").send_keys("1456723")
#     browser.find_element(By.NAME, "submit").click()
#     time.sleep(3)
#     odgovor = browser.find_element(By.TAG_NAME, "body")
#     assert odgovor.text.strip() == "Neuspesno logovanje, molim vas pokusajte ponovo"

# # C://Users/Grupa1/Qa..../Vezbe_26_06/naziv_slike.jpg - apsolutna
# # naziv_slike.jpg - relativna
# # slike/naziv_slike.jpg - relativna putanja

browser = Firefox()
def login(): # pomocna funkcija za login
    browser.get("http://gresnik.com")
    browser.find_element(By.LINK_TEXT, "Log in").click()
    time.sleep(2)
    browser.find_element(By.NAME, "user").send_keys("Autor")
    browser.find_element(By.NAME, "pass").send_keys("123")
    browser.find_element(By.NAME, "submit").click()
    time.sleep(3)

def test_objava_clanka():
    login()
    browser.find_element(By.LINK_TEXT, "Novi članak").click()
    time.sleep(2)
    # identifikovanje tekst polja po name
    # send keys (naslov, opis clanka, sadrzaj, objavljen 0/1)
    # upload slike send keys putanju
    # C:\Users\Grupa 1\Desktop\qa-grupa-1-casovi\vezbe_26_06
    browser.find_element(By.NAME,"uploadImg").send_keys("C:/Users/Grupa 1/Desktop/qa-grupa-1-casovi/vezbe_26_06/Bankomat.jpg")
    putanja = os.path.abspath("Bankomat.jpg")
    browser.find_element(By.NAME,"uploadImg").send_keys(putanja)

    # identifikacija tastera
    # klik na taster

    # odlazak na svi clanci
    # provera da li je medju naslovima uneti naslov