import threading
import time

def priprema_glavnog_jela():
    print("Pripremam glavno jelo")
    time.sleep(6)
    print("Zavrseno glavno jelo")

def priprema_priloga():
    print("Pripremam priloge")
    time.sleep(3)
    print("Zavrseni prilozi")

nit1 = threading.Thread(target=priprema_glavnog_jela)
nit2 = threading.Thread(target=priprema_priloga)

nit1.start()
nit2.start()

nit1.join()
nit2.join()
print("Posluzen sto.")