import threading
import time
# from threading import Thread

def poruka1():
    print("Hello 1")
    time.sleep(5)
    print("Zavrsena nit 1")


def poruka2():
    print("Hello iz poruke 2")
    time.sleep(7)
    print("Zavrsena nit 2")

nit = threading.Thread(target=poruka1)
nit.start()

nit2 = threading.Thread(target=poruka2)
nit2.start()

print("Zavrsetak programa") # glavna nit programa
