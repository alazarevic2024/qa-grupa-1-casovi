package org.example;

import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.junit.Assert;
import org.junit.Test;

public class IzlozbaTest {
    int brojMeseci;
    String razred;

    @Given("Postavljen je broj meseci {int}")
    public void postavljanjeBrojaMeseci(int meseci) {
        this.brojMeseci = meseci;
    }
    @When("Izracunavam razred")
    public void izracunavanje(){
        this.razred = Izlozba.odrediRazred(brojMeseci);
    }
    @Then("Ocekujem da dobijem razred {string}")
    public void proveraRezultata(String ocekivano) {
        Assert.assertEquals(ocekivano, this.razred);
    }
}
