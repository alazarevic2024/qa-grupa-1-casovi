package org.example;

public class LoginService {
    private final String validEmail = "test@primer.com";
    private final String validPassword = "sifra123";

    public String login(String email, String password) {
        if (email == null || email.isEmpty()) return "Email je obavezan";
        if (password == null || password.isEmpty()) return "Lozinka je obavezna";
        if (!email.equals(validEmail)) return "pogresan email";
        if (!password.equals(validPassword)) return "pogresna lozinka";
        return "uspesno";
    }
}
