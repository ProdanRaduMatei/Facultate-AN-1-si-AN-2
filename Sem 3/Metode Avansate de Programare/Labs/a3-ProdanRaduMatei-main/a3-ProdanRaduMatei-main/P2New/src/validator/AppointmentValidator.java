package validator;

import domain.DoctorAppointments;

public class AppointmentValidator implements Validator<DoctorAppointments> {
    @Override
    public void validate(DoctorAppointments appointments) {

        if(appointments.getId() < 0)
            throw new IllegalArgumentException("Id must be a positive number");

        if(appointments.getName() == null || appointments.getName().isEmpty())
            throw new IllegalArgumentException("Name is required");
        
        if(appointments.getSpecialization() == null || appointments.getSpecialization().isEmpty())
            throw new IllegalArgumentException("Specialty is required");
        
        if(appointments.getAddress() == null || appointments.getAddress().isEmpty())
            throw new IllegalArgumentException("Address is required");

        if(appointments.getPhone() == null || appointments.getPhone().isEmpty())
            throw new IllegalArgumentException("Phone is required");
        
        if(appointments.getIsAppointed() != true && appointments.getIsAppointed() != false)
            throw new IllegalArgumentException("Appointment status is required");
        
        if(appointments.getAppointedTime() == null || appointments.getAppointedTime().isEmpty())
            throw new IllegalArgumentException("Appointment time is required");
    }
}
