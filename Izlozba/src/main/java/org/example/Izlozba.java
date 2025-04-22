package org.example;

public class Izlozba {
    String lokacija;
    String tipIzlozbe;

    public Izlozba(String lokacija, String tipIzlozbe) {
        this.lokacija = lokacija;
        this.tipIzlozbe = tipIzlozbe;
    }

    /** "bebe" "mladi" "zreli" "netacan unos"
     *
     * @param brojMeseci
     * @return odredjeni razred
     */
    public static String odrediRazred(int brojMeseci) {
        if (brojMeseci < 3 ) {
            return "ne ucestvuje";
        } else if (brojMeseci >= 3 && brojMeseci <= 6) {
            return "bebe";
        } else if (brojMeseci > 6 && brojMeseci < 15) {
            return "mladi";
        } else if (brojMeseci >= 15 && brojMeseci < 24) {
            return "zreli";
        } else {
            return "netacan unos";
        }
    }

}
