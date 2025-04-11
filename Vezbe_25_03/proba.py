# import mysql.connector as conn

# konekcija = conn.connect(user="root", host="localhost", port=3306,database="sakila", passwd="root")


import pytest
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5