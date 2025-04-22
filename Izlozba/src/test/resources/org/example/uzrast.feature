Feature: Uzrast
  Scenario: Proveravam razred mladih
    Given Postavljen je broj meseci 10
    When Izracunavam razred
    Then Ocekujem da dobijem razred "mladi"
