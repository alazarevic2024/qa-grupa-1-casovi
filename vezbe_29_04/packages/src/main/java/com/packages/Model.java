package com.packages;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class Model {
    Map<String,Package> packages;
    public Model() {
        this.packages  = new HashMap<>();
        this.packages.put("100mb",new Package("100mb",100,500));
        this.packages.put("300mb",new Package("300mb",300,1200));
        this.packages.put("700mb",new Package("700mb",700,1500));
        this.packages.put("1GB",new Package("1GB",1000,2000));
    }
    public Package getPackage(String name){
        return this.packages.containsKey(name) ? this.packages.get(name) : null;
    }
    public Map<String,Package> getPackages(){
        return this.packages;
    }
    public void addPackage(Package p){
        this.packages.put(p.name,p);
    }
    public void updatePackage(Package p){
        if(this.packages.containsKey(p.name)){
            this.addPackage(p);
        }
    }
    public void deletePackage(Package p){
        if(this.packages.containsKey(p.name)){
            this.addPackage(p);
        }
    }

}
