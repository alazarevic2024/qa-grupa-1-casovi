#  https://github.com/alazarevic2024/qa-grupa-1-casovi.git

#  http://gresnik.com/
#  http://gresnik.com/opis.txt
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
import time
import pytest

def test_login_neispravni_korisnici():
    neispravni = [1]
    for i in neispravni:
        kor_ime = f"user_{i}"
        sifra = f"password_{i}"
        browser = Firefox()
        browser.get("http://gresnik.com/")

        kor_ime_polje = browser.find_element(By.ID, "inputEmail")
        kor_ime_polje.send_keys(kor_ime)

        sifra_polje = browser.find_element(By.NAME, "password")
        sifra_polje.send_keys(sifra)

        taster = browser.find_element(By.TAG_NAME, "button")
        taster.click()
        
        browser.get_screenshot_as_file(f"ulogovan{i}.png")

        poruka = browser.find_element(By.TAG_NAME, "body").text
        assert poruka == "User is not valid"
        browser.close()

def test_login_ispravni_korisnici():
    validni = [1, 2, 3] # ovo su ispravni sufiksi korisnika
    for i in validni:
        kor_ime = f"user_{i}"
        sifra = f"password_{i}"

        browser = Firefox()
        browser.get("http://gresnik.com/")

        kor_ime_polje = browser.find_element(By.ID, "inputEmail")
        kor_ime_polje.send_keys(kor_ime)

        sifra_polje = browser.find_element(By.NAME, "password")
        sifra_polje.send_keys(sifra)

        taster = browser.find_element(By.TAG_NAME, "button")
        taster.click()
        
        browser.get_screenshot_as_file(f"ulogovan{i}.png")

        formatiran = kor_ime.split("_")
        ocekivano = "Hello " + formatiran[0] + " " + formatiran[1]

        # Provera ulogovane strane
                # ili elemente ili None
        naslov = browser.find_element(By.TAG_NAME, "h5")
        assert naslov.text == ocekivano
        naslov_strane = browser.find_element(By.TAG_NAME, "h1")
        assert naslov_strane.text == "Pricing"
        browser.close()

# Obuhvata proveru oba scenarija i pozitivan i negativan
# Test pada samo ako ispravni podaci odvedu na neocekivanu stranu umesto Pricing
# Test pada ako neispravni podaci odvedu negde druge osim na User not valid
def test_login_strane():
    for i in range(1, 31):
        kor_ime = f"user_{i}"
        sifra   = f"password_{i}"

        browser = Firefox()
        browser.get("http://gresnik.com/")

        kor_ime_polje = browser.find_element(By.ID, "inputEmail")
        kor_ime_polje.send_keys(kor_ime)

        sifra_polje = browser.find_element(By.NAME, "password")
        sifra_polje.send_keys(sifra)

        taster = browser.find_element(By.TAG_NAME, "button")
        taster.click()
        
        browser.get_screenshot_as_file(f"ulogovan{i}.png")

        formatiran = kor_ime.split("_")
        ocekivano = "Hello " + formatiran[0] + " " + formatiran[1]

        # Provera ulogovane strane
                # ili elemente ili None
        if browser.find_elements(By.TAG_NAME, "h5"):
            naslov = browser.find_element(By.TAG_NAME, "h5")
            assert naslov.text == ocekivano
            naslov_strane = browser.find_element(By.TAG_NAME, "h1")
            assert naslov_strane.text == "Pricing"
        else:
            print("Nije ulogovan korisnik")
            poruka = browser.find_element(By.TAG_NAME, "body").text
            assert poruka == "User not valid"

        browser.close()