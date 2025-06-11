import threading
# from threading import Thread, Lock
import time

instrumenti = ["gitara", "violina", "kahon"]

katanac = threading.Lock()

def svirka(instrument):
  
    print(f"Trenutno svira {instrument}")
    if instrument == "gitara":
        time.sleep(5)
    elif instrument == "violina":
        time.sleep(5)
    elif instrument == "kahon":
        time.sleep(5)
    print(f"Zavrsio je {instrument}")

    katanac.acquire() # zakljucava 
    print(f"Poklonio se {instrument}") # samo jedna pristupa
    katanac.release() # otkljucava i dozvoljava dalje


for instrument in instrumenti:
    nit = threading.Thread(target=svirka, args=[instrument])
    nit.start()