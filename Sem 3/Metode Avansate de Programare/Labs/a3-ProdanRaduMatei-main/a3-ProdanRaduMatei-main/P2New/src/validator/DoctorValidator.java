package validator;

import domain.Doctor;

public class DoctorValidator implements Validator<Doctor> {
    @Override
    public void validate(Doctor doctor) {
        if(doctor.getId() < 0)
            throw new IllegalArgumentException("Id must be a positive number");
        
        if(doctor.getName() == null || doctor.getName().isEmpty())
            throw new IllegalArgumentException("Name is required");

        if(doctor.getPhone() == null || doctor.getPhone().isEmpty())
            throw new IllegalArgumentException("Phone is required");

        if(doctor.getAddress() == null || doctor.getAddress().isEmpty())
            throw new IllegalArgumentException("Address is required");

        if(doctor.getSpecialization() == null || doctor.getSpecialization().isEmpty())
            throw new IllegalArgumentException("Specialty is required");
    }
}
