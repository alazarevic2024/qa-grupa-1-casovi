package org.example;

public class Bend {
    private String naziv;
    private int satnica;

    // napravi instancu benda
    public Bend (String naziv, int satnica) {
        this.naziv = naziv;
        this.satnica = satnica;
    }

    public int izracunajZaradu(int trajanje) {
        int zarada = this.satnica * trajanje;
        return zarada;
    }

    public String vratiInformacijeOBendu() {
        String informacije = "Ime benda: " + naziv;
        return informacije;
    }
}
