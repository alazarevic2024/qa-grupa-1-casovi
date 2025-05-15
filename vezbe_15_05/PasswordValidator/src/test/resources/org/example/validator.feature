Feature: PasswordValidator

    Scenario Outline:
      Given korisnik unosi password "<sifra>"
      When vrsimo validaciju
      Then ocekujemo "<rezultat>"

      Examples:
      |sifra   |rezultat|
      |Test1234|uspesno |
      |test1234|neuspesno|
      |test    |neuspesno|