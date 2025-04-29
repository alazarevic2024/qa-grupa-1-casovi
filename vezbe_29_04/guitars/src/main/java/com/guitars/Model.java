package com.guitars;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class Model {
    Map<String,Guitar> guitars;
    public Model() {
        this.guitars  = new HashMap<>();
        this.guitars.put("Fender Stratocaster",new Guitar("Fender Stratocaster",1200));
        this.guitars.put("Ibanez Jem",new Guitar("Ibanez Jem",3400));
        this.guitars.put("Gibson Les Paul",new Guitar("Gibson Les Paul",4100));
        this.guitars.put("Music Man",new Guitar("Music Man",4350));
    }

    /**
     *
     * @param name - prosledjuje se naziv gitare
     * @return - vraca Guitar - dobijenu gitaru ako postoji
     */
    public Guitar getGuitar(String name){
        return this.guitars.containsKey(name) ? this.guitars.get(name) : null;
    }

    /*
     Ovo je obican komentar
     */
    public Map<String,Guitar> getGuitars(){
        return this.guitars;
    }

    public void addGuitar(Guitar g){
        this.guitars.put(g.name,g);
    }

    public void updateGuitar(Guitar g){
        if(this.guitars.containsKey(g.name)){
            this.addGuitar(g);
        }
    }
    public void deleteGuitar(Guitar g){
        if(this.guitars.containsKey(g.name)){
            this.addGuitar(g);
        }
    }

}
