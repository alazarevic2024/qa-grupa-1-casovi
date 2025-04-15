package org.example;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

public class BendTest {
    Bend bend;
    @Before
    public void setUp() {
        bend = new Bend("Nicim izazvan", 100);
        System.out.println("Izvrsavam pre testa");
    }

    @Test
    public void zaradaTest() {
        int trajanje = 3;
        int ocekivano = 300;
        int dobijeno = bend.izracunajZaradu(trajanje);
        Assert.assertEquals(ocekivano, dobijeno);
    }
}
