//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        /*
        int a = 2;
        int b = 3;
        int c = a + b;
        System.out.println(c);
        */
//        Utakmica u = new Utakmica();
//        u.pocetak();
//        u.kraj();
//        Utakmica u = new Utakmica();
//        int duzina = u.duzina_poluvremena();
//        System.out.println(duzina);

        Utakmica u = new Utakmica();
        int ocekivano = 45;
        int dobijeno = u.duzina_poluvremena();

        boolean rezultat_testa =  ocekivano == dobijeno;
        System.out.println(rezultat_testa);


    }
}