# http://javascript.rs:8000/set-lang
import requests

odgovor = requests.get("http://javascript.rs:8000", headers={"Cookie":"sr"})
print(odgovor.text)



# http://javascript.rs:8000/set-theme?value=dark