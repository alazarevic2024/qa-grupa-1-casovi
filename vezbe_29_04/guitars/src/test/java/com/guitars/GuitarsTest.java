package com.guitars;

import org.junit.Assert;
import org.junit.Test;

public class GuitarsTest {
    @Test
    public void testGetSingleGuitar() {
        Model modelSaGitarama = new Model();
        Guitar gitara = modelSaGitarama.getGuitar("Ibanez Jem");
        Assert.assertEquals(gitara.name, "Ibanez Jem");
        Assert.assertEquals(3400,gitara.price, 0);
    }

    // Provera da li se vraca null kad gitara ne postoji

    // Provera da li radi dodavanje gitare
    @Test
    public void testAddGuitar(){
        Model modelSaGitarama = new Model(); // on sadrzi logiku za dodavanje, brisanje, izmenu

        // instanca gitare sa svojim vrednostima
        Guitar mojaGitara = new Guitar("No name model", 1000);

        // dodavanje
        modelSaGitarama.addGuitar(mojaGitara);

        // provera da li je dodata kreirana gitara mojaGitara
        Guitar dodataGitara = modelSaGitarama.getGuitar("No name model");
        // proveravam da li je uopste nesto uneto
        Assert.assertNotNull(dodataGitara);

        // Proveravam da li se uneta gitara poklapa sa kreiranom koju smo
        // zeleli da unesemo
        Assert.assertEquals(dodataGitara.name, mojaGitara.name);
        Assert.assertEquals(mojaGitara.price,dodataGitara.price, 0);
    }

}
