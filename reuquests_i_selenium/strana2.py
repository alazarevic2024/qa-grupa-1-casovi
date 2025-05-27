from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# ispravni podaci: ana   |    loznika123
browser = webdriver.Firefox()
browser.get("http://gubitnik.com/p2/forma1.php")
time.sleep(3)
kor_ime = browser.find_element(By.ID, "username")
kor_ime.send_keys("ana")
time.sleep(2)

sifra = browser.find_element(By.ID, "password")
sifra.send_keys("lozinka123")
time.sleep(2)

taster = browser.find_element(By.TAG_NAME, "button")
taster.click()

time.sleep(5)
rezultat = browser.find_element(By.CLASS_NAME, "welcome")
print(rezultat.text == "Dobrodošao, ana!")
boja_teksta = rezultat.value_of_css_property("color")
print(boja_teksta)