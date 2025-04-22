package org.example;

public class Pas {
    private String ime;
    String rasa;
    int brojMeseci;

    public Pas(String ime, String rasa, int brojMeseci) {
        this.ime = ime;
        this.rasa = rasa;
        this.brojMeseci = brojMeseci;
    }

    public String getIme() {
        return this.ime;
    }

    public void setIme(String dobijenoIme) {
        this.ime = dobijenoIme;
    }

}
