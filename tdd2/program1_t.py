import program1 as pr

# unit test
def provera_izmene_cene():
    cena = 100 # zeljena cena
    ocekivana_cena_sa_porezom = 120 # ocekivano nakon dodavanja poreza
    jelo = pr.Jelo("Corba", 0)
    jelo.promeni_cenu_sa_porezom(cena)
    # provera ocekivano da li je jednako sa dobijenim
    print(ocekivana_cena_sa_porezom == jelo.cena)

provera_izmene_cene()