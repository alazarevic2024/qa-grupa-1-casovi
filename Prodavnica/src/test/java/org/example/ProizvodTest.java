package org.example;

import org.junit.Assert;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;

public class ProizvodTest {

    static Proizvod proizvod;

    @BeforeClass
    public static void setUp() {
        proizvod = new Proizvod("Mis", 100);
    }

    @Test
    public void cenaSaPorezomTest(){
        double ocekivano = 120;
        double dobijeno = proizvod.izracunajCenuSaPorezom(20);
        Assert.assertEquals(ocekivano, dobijeno, 0);
    }

    @Test
    public void cenaSaPopustomTest() {
        double ocekivano = 80;
        double dobijeno = proizvod.izracunajCenuSaPopustom(20);
        Assert.assertEquals(ocekivano, dobijeno, 0);
    }
}
