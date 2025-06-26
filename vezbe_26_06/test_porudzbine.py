# http://gubitnik.com/porudzbine.html
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
import time
import pytest

# Test Case - ispravno popunjena forma i poredjenje rezultata
def test_ispravno_popunjeni_podaci():
    # postavljene test vrednosti
    ime_test = "Marko"
    email_test = "proba@gmail.com"
    odabrani_proizvodi = ["Laptop", "Kamera"]

    browser = Firefox()
    browser.get("http://gubitnik.com/porudzbine.html")
    # upis imena u tekst polje za ime i prezime
    browser.find_element(By.ID, "name").send_keys(ime_test)
    # upis emaila u tekst polje za email
    email_polje = browser.find_element(By.ID, "email")
    email_polje.send_keys(email_test)

    checkboxovi = browser.find_elements(By.NAME, "product")
    # checkboxovi = browser.find_elements(By.XPATH, "//input[@type='checkbox']")
    # prolazak kroz dobijene cekboksove i interakcija
    for boks in checkboxovi:
        if boks.get_attribute("value") in odabrani_proizvodi:
            boks.click()

    # identifikacija tastera i interakcija
    taster = browser.find_element(By.ID, "finish-btn")
    taster.click() #ako ima dodatne interakcije / provere
    time.sleep(5)

    naslov = browser.find_element(By.TAG_NAME, "h3").text.strip()
    ocekivano = "Hvala, Marko!"
    assert naslov == ocekivano

    str_tagovi = browser.find_elements(By.TAG_NAME, "strong")
    assert str_tagovi[0].text.strip() == email_test

    ocekivani_proizvodi = f"{odabrani_proizvodi[0]}, {odabrani_proizvodi[1]}"
    # "Kamera, Laptop"

    ocekivani_proizvodi = ""
    for i in range(len(odabrani_proizvodi)):
        if i < len(odabrani_proizvodi) - 1:
            ocekivani_proizvodi += f"{odabrani_proizvodi[i]}, "
        else:
            ocekivani_proizvodi += f"{odabrani_proizvodi[i]}"

    assert str_tagovi[1].text.strip() == ocekivani_proizvodi

def test_poslata_prazna_forma():
    pass
    # send keys ime ""
    # send keys za email ""
    # check boxove ne cekiram
    # klik na taster Zavrsi narudzbinu
    # provera ocekivano == dobijeno