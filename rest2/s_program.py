from flask import Flask, request
import jwt
import time

app = Flask("Logovanje")

# base url + /ruta
validni_korisnici = {
    "gost":"1234",
    "admin":"456"
}

tajni_kljuc = "1234abcd"

@app.route("/login", methods=["POST"])
def login_korisnika():
    podaci = request.get_json() # izvlacimo body koji je dosao do servera
    username = podaci["username"] # ovo smo dobili u body
    password = podaci["password"] # ovo smo dobili u body

    if username in validni_korisnici and validni_korisnici[username] == password:
        isticanje = time.time() + 30
        token_za_korisnika = jwt.encode({"un":username,"ulogovan":True, "exp":isticanje}, key=tajni_kljuc, algorithm="HS256")
        return {"success":"true", "message":f"Dobro dosao {username}", "token":token_za_korisnika}
    else:
        return {"success":"false", "message":"Netacni podaci!"}
    
@app.route("/proizvodi")
def prikazi_proizvode():
    try:
        dobijeni_token = request.headers["Authorization"] # ovo salje korisnik
        podaci = jwt.decode(dobijeni_token, key=tajni_kljuc, algorithms=["HS256"])
        return {"korisnik":f"{podaci["un"]}", "proizvodi": ["Laptop", "Telefon", "Punjac"]}
    except jwt.ExpiredSignatureError:
        return "Token je istekao"
    except jwt.InvalidTokenError:
        return "Token nije validan"

app.run(host="127.0.0.1")
