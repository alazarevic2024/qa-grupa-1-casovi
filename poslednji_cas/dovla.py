import requests

# odgovor = requests.get("http://gresnik.com/api.php").text
# print(odgovor)

import requests 

odgovor = requests.get("https://it-akademija.com").text

print(odgovor)