import pytest
import calc
# from calc import mul, add, div

# testira metod mul iz fajla calc
# prosledjujemo 2 broja i poredimo ocekivano sa dobijenim
def test_mnozenje():
    ocekivano = 35
    dobijeno  = calc.mul(5, 7)
    assert dobijeno == ocekivano

def test_sabiranje():
    assert 10 == calc.add(5, 5)