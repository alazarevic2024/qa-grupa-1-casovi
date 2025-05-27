from selenium import webdriver
from selenium.webdriver.common.by import By
import getpass
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()
browser.get("https://it-akademija.com/dls")

wait = WebDriverWait(browser, 10) #maksimamlno cekanje

kor_ime_tp = browser.find_element(By.ID, "username")
kor_ime_tp.send_keys("ita22.aleksandra.probni")

password_tp = browser.find_element(By.ID, "password")
sifra = getpass.getpass("Unesite sifru: ")
password_tp.send_keys(sifra)

# By.NAME "subPrijava" - po nazivu
# XPath
taster = browser.find_element(By.XPATH,"//input[@id='submit']") 
taster.click()

import time
time.sleep(10)

podrska_ucenju = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Podrška učenju")))
podrska_ucenju.click()
time.sleep(10)
video_arhiva = browser.find_element(By.LINK_TEXT, "Video arhiva ")
video_arhiva.click()


