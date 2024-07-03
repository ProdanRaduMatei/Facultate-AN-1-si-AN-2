package domain;

import java.io.Serializable;

public class DoctorAppointments implements Identifiable<Integer>, Serializable {
    Integer id, doctorId, patientId;
    private String specialization, appointedTime;

    public DoctorAppointments(Integer id, Integer doctorId, Integer patientId, String specialization, String appointedTime) {
        this.id = id;
        this.doctorId = doctorId;
        this.patientId = patientId;
        this.specialization = specialization;
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
                ", doctorId = " + doctorId +
                ", patientId = " + patientId +
                ", specialization = " + specialization +
                ", appointedTime = " + appointedTime + " }";
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

    public Integer getDoctorId() {
        return doctorId;
    }

    public Integer getPatientId() {
        return patientId;
    }

    public String getSpecialization() {
        return specialization;
    }

    public String getAppointedTime() {
        return appointedTime;
    }

    public void setDoctorId(Integer doctorId){
        this.doctorId = doctorId;
    }

    public void setPatientId(Integer patientId){
        this.patientId = patientId;
    }

    public void setSpecialization(String specialization){
        this.specialization = specialization;
    }

    public void setAppointedTime(String appointedTime){
        this.appointedTime = appointedTime;
    }
}
