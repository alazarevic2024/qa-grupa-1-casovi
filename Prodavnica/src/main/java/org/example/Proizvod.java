package org.example;

public class Proizvod {
    String naziv;
    double cena;


    public Proizvod (String naziv, double cena) {
        this.naziv = naziv;
        this.cena = cena;
    }

    public double izracunajCenuSaPorezom(double porez) {
        double cenaSaPorezom = this.cena + this.cena * (porez / 100);
        return cenaSaPorezom;
    }

    public double izracunajCenuSaPopustom(double popust) {
        double cenaSaPopustom = this.cena - this.cena * (popust / 100);
        return cenaSaPopustom;
    }
}
