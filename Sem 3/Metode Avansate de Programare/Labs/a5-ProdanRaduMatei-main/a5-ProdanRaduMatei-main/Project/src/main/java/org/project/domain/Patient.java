package org.project.domain;

import java.util.Objects;

public class Patient implements Identifiable<Integer> {
    private Integer id;
    private String name, phone, address, illness, treatment;

    public Patient(Integer id, String name, String phone, String address, String illness, String treatment) {
        this.id = id;
        this.name = name;
        this.phone = phone;
        this.address = address;
        this.illness = illness;
        this.treatment = treatment;
    }

    public String getName() {
        return name;
    }

    public String getPhone() {
        return phone;
    }

    public String getAddress(){
        return address;
    }

    public String getIllness(){
        return illness;
    }

    public String getTreatment(){
        return treatment;
    }

    public void setName(String name){
        this.name = name;
    }

    public void setPhone(String phone){
        this.phone = phone;
    }

    public void setAddress(String address){
        this.address = address;
    }

    public void setIllness(String illness){
        this.illness = illness;
    }

    public void setTreatment(String treatment){
        this.treatment = treatment;
    }

    @Override
    public Integer getId() {
        return id;
    }

    @Override
    public void setId(Integer id) {
        this.id = id;
    }

    @Override
    public String toString() {
        return "Patient[" + "id: " + id + ", name: " + name + ", phone: " + phone + ", address: " + address + ", illness: " + illness + ", treatment: " + treatment + ']';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o)
            return true;
        if (o == null || o.getClass() != this.getClass())
            return false;
        Patient patient = (Patient) o;
        return Objects.equals(id, patient.id);
    }
}
