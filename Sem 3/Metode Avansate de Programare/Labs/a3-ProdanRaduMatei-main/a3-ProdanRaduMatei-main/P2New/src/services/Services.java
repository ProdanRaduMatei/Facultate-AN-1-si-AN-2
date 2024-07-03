package services;

import java.io.FileInputStream;
import java.util.ArrayList;
import java.util.Properties;

import domain.DoctorAppointments;
import repository.DoctorAppointmentsRepositoryBinaryFile;
import repository.DoctorAppointmentsRepositoryTextFile;
import repository.DoctorRepositoryBinaryFile;
import repository.PatientRepositoryBinaryFile;
import repository.PatientRepositoryTextFile;
import repository.DoctorRepositoryTextFile;
import repository.IRepository;
import repository.MemoryRepository;
import domain.Doctor;
import domain.Patient;
import validator.*;

public class Services {
    private IRepository<Integer, DoctorAppointments> appointmentsRepo;
    private IRepository<Integer, Doctor> doctorsRepo;
    private IRepository<Integer, Patient> patientsRepo;
    private Validator<DoctorAppointments> appointmentsValidator;
    private Validator<Doctor> doctorsValidator;
    private Validator<Patient> patientsValidator;

    public Services() {
        Properties properties = new Properties();
        String settingsName = "P2New/src/settings.properties";
        try (FileInputStream fileInputStream = new FileInputStream(settingsName)) {
            properties.load(fileInputStream);
            System.out.println("Settings loaded from " + settingsName);
        } catch (Exception e) {
            System.out.println("Cannot find " + settingsName + ": " + e);
        }
        String appointmentsFile = properties.getProperty("Appointments");
        String doctorsFile = properties.getProperty("Doctors");
        String patientsFile = properties.getProperty("Patients");
        String repositoryType = properties.getProperty("Repository");
        if (repositoryType != null && repositoryType.equals("text")) {
            appointmentsRepo = new DoctorAppointmentsRepositoryTextFile(appointmentsFile);
            doctorsRepo = new DoctorRepositoryTextFile(doctorsFile);
            patientsRepo = new PatientRepositoryTextFile(patientsFile);
        }
        else if (repositoryType != null && repositoryType.equals("binary")) {
            appointmentsRepo = new DoctorAppointmentsRepositoryBinaryFile(appointmentsFile);
            doctorsRepo = new DoctorRepositoryBinaryFile(doctorsFile);
            patientsRepo = new PatientRepositoryBinaryFile(patientsFile);
        }
        else {
            appointmentsRepo = new MemoryRepository<>();
            doctorsRepo = new MemoryRepository<>();
            patientsRepo = new MemoryRepository<>();
        }
        appointmentsValidator = new AppointmentValidator();
        doctorsValidator = new DoctorValidator();
        patientsValidator = new PatientValidator();
    }

    public void initAppointmentsRepo() {
        if (this.appointmentsRepo != null) {
            appointmentsRepo.add(new DoctorAppointments(1, "John Doe", "Cardiology", "Cluj", "0712345678", false, "2023.01.01"));
            appointmentsRepo.add(new DoctorAppointments(2, "Jane Doe", "Neurology", "Cluj", "0712345678", false, "2023.01.01"));
            appointmentsRepo.add(new DoctorAppointments(3, "John Smith", "Cardiology", "Cluj", "0712345678", false, "2023.01.01"));
            appointmentsRepo.add(new DoctorAppointments(4, "Jane Smith", "Neurology", "Cluj", "0712345678", false, "2023.01.01"));
        }
        else
            System.out.println("Repository is not initialized!");
    }

    public void initDoctorsRepo() {
        if (this.doctorsRepo != null) {
            doctorsRepo.add(new Doctor(1, "John Doe", "0712345678", "Cluj", "Cardiology"));
            doctorsRepo.add(new Doctor(2, "Jane Doe", "0712345678", "Cluj", "Neurology"));
            doctorsRepo.add(new Doctor(3, "John Smith", "0712345678", "Cluj", "Cardiology"));
            doctorsRepo.add(new Doctor(4, "Jane Smith", "0712345678", "Cluj", "Neurology"));
        } else {
            System.out.println("Doctors repository is not initialized!");
        }
    }

    public void initPatientsRepo() {
        if (this.patientsRepo != null) {
            patientsRepo.add(new Patient(1, "John Doe", "0712345678", "Cluj", "cough", "medication"));
            patientsRepo.add(new Patient(2, "Jane Doe", "0712345678", "Cluj", "headache", "medication"));
            patientsRepo.add(new Patient(3, "John Smith", "0712345678", "Cluj", "fever", "medication"));
            patientsRepo.add(new Patient(4, "Jane Smith", "0712345678", "Cluj", "cough", "medication"));
        } else {
            System.out.println("Patients repository is not initialized!");
        }
    }

    public void addAppointment(Integer id, String name, String specialization, String address, String phone, Boolean isAppointed, String appointedTime) {
        DoctorAppointments newAppointment = new DoctorAppointments(id, name, specialization, address, phone, isAppointed, appointedTime);
        appointmentsValidator.validate(newAppointment);
        appointmentsRepo.add(newAppointment);
    }

    public void addDoctor(Integer id, String name, String phone, String address, String specialization) {
        Doctor newDoctor = new Doctor(id, name, phone, address, specialization);
        doctorsValidator.validate(newDoctor);
        doctorsRepo.add(newDoctor);
    }

    public void addPatient(Integer id, String name, String phone, String address, String illness, String treatment) {
        Patient newPatient = new Patient(id, name, phone, address, illness, treatment);
        patientsValidator.validate(newPatient);
        patientsRepo.add(newPatient);
    }

    public void removeAppointment(Integer id) {
        appointmentsRepo.delete(id);
    }

    public void removeDoctor(Integer id) {
        doctorsRepo.delete(id);
    }

    public void removePatient(Integer id) {
        patientsRepo.delete(id);
    }

    public void updateAppointment(Integer id, String name, String specialization, String address, String phone, boolean isAppointed, String appointedTime) {
        DoctorAppointments newAppointment = new DoctorAppointments(id, name, specialization, address, phone, isAppointed, appointedTime);
        appointmentsValidator.validate(newAppointment);
        appointmentsRepo.update(id, newAppointment);
    }

    public void updateDoctor(Integer id, String name, String phone, String address, String specialization) {
        Doctor newDoctor = new Doctor(id, name, phone, address, specialization);
        doctorsValidator.validate(newDoctor);
        doctorsRepo.update(id, newDoctor);
    }

    public void updatePatient(Integer id, String name, String phone, String address, String illness, String treatment) {
        Patient newPatient = new Patient(id, name, phone, address, illness, treatment);
        patientsValidator.validate(newPatient);
        patientsRepo.update(id, newPatient);
    }

    public DoctorAppointments findAppointmentsById(Integer id) {
        return appointmentsRepo.findByID(id);
    }

    public Doctor findDoctorById(Integer id) {
        return doctorsRepo.findByID(id);
    }

    public Patient findPatientById(Integer id) {
        return patientsRepo.findByID(id);
    }

    public ArrayList<DoctorAppointments> getAllAppointments() {
        ArrayList<DoctorAppointments> appointmentsList = new ArrayList<>();
        Iterable<DoctorAppointments> appointments = appointmentsRepo.getAll();
        for(DoctorAppointments a : appointments) {
            appointmentsList.add(a);
        }
        return appointmentsList;
    }

    public ArrayList<Doctor> getAllDoctors() {
        ArrayList<Doctor> doctorsList = new ArrayList<>();
        Iterable<Doctor> doctors = doctorsRepo.getAll();
        for(Doctor d : doctors) {
            doctorsList.add(d);
        }
        return doctorsList;
    }

    public ArrayList<Patient> getAllPatients() {
        ArrayList<Patient> patientsList = new ArrayList<>();
        Iterable<Patient> patients = patientsRepo.getAll();
        for(Patient p : patients) {
            patientsList.add(p);
        }
        return patientsList;
    }
}
