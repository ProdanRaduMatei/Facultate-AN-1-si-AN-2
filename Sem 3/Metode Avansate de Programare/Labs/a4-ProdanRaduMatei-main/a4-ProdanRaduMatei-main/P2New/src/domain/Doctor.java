package domain;

import java.io.Serializable;
import java.util.Objects;

public class Doctor implements Identifiable<Integer>, Serializable{
    private Integer id;
    private String name, phone, address, specialization;

    @Override
    public Integer getId() {
        return this.id;
    }

    @Override
    public void setId(Integer id) {
        this.id = id;
    }

    public Doctor(int id, String name, String phone, String address, String specialization) {
        this.id = id;
        this.name = name;
        this.phone = phone;
        this.address = address;
        this.specialization = specialization;
    }

    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setAddress(String address){
        this.address = address;
    }

    public String getAddress(){
        return this.address;
    }

    public void setPhone(String phone){
        this.phone = phone;
    }

    public String getPhone(){
        return this.phone;
    }

    public void setSpecialization(String specialization){
        this.specialization = specialization;
    }

    public String getSpecialization(){
        return this.specialization;
    }

    @Override
    public String toString() {
        return "Doctor{" +
                "id: " + id +
                ", name: " + name +
                ", phone: " + phone +
                ", address: " + address +
                ", specialization: " + specialization +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o)
            return true;
        if (o == null || getClass() != o.getClass())
            return false;
        Doctor doctor = (Doctor) o;
        return Objects.equals(id, doctor.id);
    }

    @Override
    public int hashCode() {
        return id;
    }
}


