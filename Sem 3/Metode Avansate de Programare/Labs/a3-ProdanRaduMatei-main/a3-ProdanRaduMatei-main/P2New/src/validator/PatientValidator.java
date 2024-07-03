package validator;

import domain.Patient;

public class PatientValidator implements Validator<Patient> {
    @Override
    public void validate(Patient patient) {

        if(patient.getId() < 0)
            throw new IllegalArgumentException("Id must be a positive number");

        if(patient.getName() == null || patient.getName().isEmpty())
            throw new IllegalArgumentException("Name is required");

        if(patient.getPhone() == null || patient.getPhone().isEmpty())
            throw new IllegalArgumentException("Phone is required");

        if(patient.getAddress() == null || patient.getAddress().isEmpty())
            throw new IllegalArgumentException("Address is required");

        if(patient.getIllness() == null || patient.getIllness().isEmpty())
            throw new IllegalArgumentException("Illness is required");

        if(patient.getTreatment() == null || patient.getTreatment().isEmpty())
            throw new IllegalArgumentException("Treatment is required");
    }
}
