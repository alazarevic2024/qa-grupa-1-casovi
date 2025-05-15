from bs4 import BeautifulSoup

moja_strana = """
<html>

<body>
    <h1>Pozdrav sa prve stranice</h1>
    <p>Ovo je <b>prvi</b> <i>pasus</i> na strani...</p>
   
    <ul id = "moja_lista">
        <li> <a href="https://it-akademija.com">IT akademija</a>    </li>
        <li> <a href="https://google.com">Google</a>    </li>
        <li>Treca stavka</li>
    </ul>

</body>

</html>
"""
strana = BeautifulSoup(moja_strana,"html.parser")
ocekivani_naslov = "Pozdrav sa prve stranice"
dobijeni_naslov = strana.find("h1").text
assert ocekivani_naslov == dobijeni_naslov

lista = strana.find("ul")
print(lista["id"])
print(lista.find("li").text.strip())

a_tag = strana.find("a")
print(a_tag["href"])
a_tagovi = strana.find_all("a")
print(a_tagovi)