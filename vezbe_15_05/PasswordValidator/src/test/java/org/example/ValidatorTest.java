package org.example;

import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.junit.Assert;

public class ValidatorTest {

    PasswordValidator validator = new PasswordValidator();
    String unetiPassword;
    String rezultat;

    @Given("korisnik unosi password {string}")
    public void korisnik_unosi_password(String string) {
       this.unetiPassword = string;
    }
    @When("vrsimo validaciju")
    public void vrsimo_validaciju() {
        this.rezultat = validator.isValid(this.unetiPassword);
    }
    @Then("ocekujemo {string}")
    public void ocekujemo_uspesnu_validaciju(String ocekivano) {
       Assert.assertEquals(ocekivano, this.rezultat);
    }
}
