package org.example;

public class PasswordValidator {
    public String isValid(String password) {
        if (password.length() < 8) return "neuspesno";
        if (!password.matches(".*[A-Z].*")) return "neuspesno";
        if (!password.matches(".*[0-9].*")) return "neuspesno";
        return "uspesno";
    }
}
