package domain;

import java.io.Serializable;

public class DoctorAppointments implements Identifiable<Integer>, Serializable {
    Integer id;
    private String name, specialization, address, phone;
    boolean isAppointed;
    String appointedTime;

    public DoctorAppointments(Integer id, String name, String specialization, String address, String phone, boolean isAppointed, String appointedTime) {
        this.id = id;
        this.name = name;
        this.specialization = specialization;
        this.address = address;
        this.phone = phone;
        this.isAppointed = isAppointed;
        this.appointedTime = appointedTime;
    }

    @Override
    public Integer getId() {
        return this.id;
    }

    @Override
    public void setId(Integer id){
        this.id = id;
    }

    @Override
    public String toString() {
        String rez = "DoctorAppointments { " +
                "id = " + id +
                ", name = '" + name + '\'' +
                ", specialization = '" + specialization + '\'' +
                ", address = '" + address + '\'' +
                ", phone = '" + phone + '\'';
        if (this.isAppointed == false)
            rez += ", not appointed";
        else
            rez += ", appointed until " + this.appointedTime;
        rez += " }";
        return rez;
    }

    @Override
    public int hashCode() {
        return id;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o)
            return true;
        if (o == null || o.getClass() != this.getClass())
            return false;
        DoctorAppointments doctorReservation = (DoctorAppointments) o;
        if (doctorReservation.getId() == this.getId())
            return true;
        return false;
    }

    public String getName() {
        return name;
    }

    public String getSpecialization() {
        return specialization;
    }

    public String getAddress() {
        return address;
    }

    public String getPhone() {
        return phone;
    }

    public boolean getIsAppointed() {
        return isAppointed;
    }

    public String getAppointedTime() {
        return appointedTime;
    }

    public void setName(String name){
        this.name = name;
    }

    public void setSpecialization(String specialization){
        this.specialization = specialization;
    }

    public void setAddress(String address){
        this.address = address;
    }

    public void setPhone(String phone){
        this.phone = phone;
    }

    public void setIsAppointed(boolean isAppointed){
        this.isAppointed = isAppointed;
    }

    public void setAppointedTime(String appointedTime){
        this.appointedTime = appointedTime;
    }
}
