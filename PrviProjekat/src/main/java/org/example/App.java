package org.example;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        Bend bend = new Bend("Nicim izazvan", 100);
        System.out.println( bend.vratiInformacijeOBendu());

        int zarada = bend.izracunajZaradu(3);
        System.out.println(zarada);
    }
}
