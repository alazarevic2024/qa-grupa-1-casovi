from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# http://gubitnik.com/p1/strana1.html
browser = webdriver.Firefox()
browser.get("http://gubitnik.com/p1/strana1.html")
naslov = browser.find_element(By.TAG_NAME, "h1")
print(naslov.text)
lista = browser.find_element(By.ID, "vehicle-list")
print(lista)

ime = "Test korisnik" # ovo unosim u tekst polje
ocekivana_poruka = f"Hello, {ime}!" # ovo ocekujem posle u rezultatu

tekst_polje = browser.find_element(By.ID, "nameInput")
tekst_polje.send_keys(ime)

taster = browser.find_element(By.ID, "greetBtn")
time.sleep(10)
taster.click()

rezultat = browser.find_element(By.ID, "result")
dobijeno = rezultat.text.strip()

print(dobijeno == ocekivana_poruka)

time.sleep(20)

browser.close()
