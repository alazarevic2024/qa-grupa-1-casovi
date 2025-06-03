import jwt

kljuc = "abcd1234"

token = jwt.encode({"success":"true"}, key=kljuc, algorithm="HS256")
print(token)

desifrovano = jwt.decode(token, kljuc, algorithms=["HS256"])
print(desifrovano)