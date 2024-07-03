package ui;

import java.util.Scanner;

import services.Services;
import domain.DoctorAppointments;
import domain.Doctor;
import domain.Patient;

public class UI {
    private Services service = new Services();

    public UI() {
        service = new Services();
    }

    public void displayMenu() {
        System.out.println("1. Add Appointment");
        System.out.println("2. Remove Appointment");
        System.out.println("3. Update Appointment");
        System.out.println("4. Find Appointment by ID");
        System.out.println("5. Get all Appointments");
        System.out.println("6. Add Doctor");
        System.out.println("7. Remove Doctor");
        System.out.println("8. Update Doctor");
        System.out.println("9. Find Doctor by ID");
        System.out.println("10. Get all Doctors");
        System.out.println("11. Add Patient");
        System.out.println("12. Remove Patient");
        System.out.println("13. Update Patient");
        System.out.println("14. Find Patient by ID");
        System.out.println("15. Get all Patients");
        System.out.println("16. Get all the appointments for a certain patient");
        System.out.println("17. Get all the appointments for a certain doctor");
        System.out.println("18. Get the problems of a certain patient");
        System.out.println("19. Get the phone number of a certain patient (given by id)");
        System.out.println("20. Get the treatment of a certain patient (given by id)");
        System.out.println("0. Exit");
    }

    public void run() {
        service.initAppointmentsRepo();
        service.initDoctorsRepo();
        service.initPatientsRepo();
        while (true) {
            this.displayMenu();
            System.out.println("Enter your choice: ");
            Scanner input = new Scanner(System.in);
            int choice = input.nextInt();
            switch(choice) {
                case 0:
                    System.out.println("Bye!");
                    input.close();
                    return;
                case 1:
                    System.out.println("Enter the details of the appointment:");
                    System.out.print("ID: ");
                    int id = input.nextInt();
                    System.out.print("Doctor ID: ");
                    int docId = input.nextInt();
                    System.out.print("Patient ID: ");
                    int patId = input.nextInt();
                    System.out.print("Specialization: ");
                    String specialization = input.next();
                    System.out.print("Appointed Time: ");
                    String appointedTime = input.next();
                    service.addAppointment(id, docId, patId, specialization, appointedTime);
                    break;
                case 2:
                    System.out.println("Enter ID of appointment to remove:");
                    int removeId = input.nextInt();
                    service.removeAppointment(removeId);
                    break;
                case 3:
                    System.out.println("Enter ID of appointment to update: ");
                    int updateId = input.nextInt();
                    System.out.println("Enter details of appointment to update:");
                    System.out.print("Doctor ID: ");
                    int newDocId = input.nextInt();
                    System.out.print("Patient ID: ");
                    int newPatId = input.nextInt();
                    System.out.print("Specialization: ");
                    String newSpecialization = input.next();
                    System.out.print("Appointed Time: ");
                    String newAppointedTime = input.next();
                    service.updateAppointment(updateId, newDocId, newPatId, newSpecialization, newAppointedTime);
                    break;
                case 4:
                    System.out.println("Enter ID of appointment to find:");
                    int findId = input.nextInt();
                    System.out.println(service.findAppointmentsById(findId));
                    break;
                case 5:
                    System.out.println("All Appointments: ");
                    for (DoctorAppointments app : service.getAllAppointments())
                        System.out.println(app);
                    break;
                case 6:
                    System.out.println("Enter details of doctor to add:");
                    System.out.print("ID: ");
                    int docid = input.nextInt();
                    System.out.print("Name: ");
                    String docname = input.next();
                    System.out.print("Phone: ");
                    String docphone = input.next();
                    System.out.print("Specialization: ");
                    String docspecialization = input.next();
                    System.out.print("Address: ");
                    String docaddress = input.next();
                    service.addDoctor(docid, docname, docphone, docaddress, docspecialization);
                    break;
                case 7:
                    System.out.println("Enter ID of doctor to remove:");
                    int docremoveId = input.nextInt();
                    service.removeDoctor(docremoveId);
                    break;
                case 8:
                    System.out.println("Enter ID of doctor to update: ");
                    int docupdateId = input.nextInt();
                    System.out.println("Enter details of doctor to update:");
                    System.out.print("Name: ");
                    String docnewName = input.next();
                    System.out.print("Phone: ");
                    String docnewPhone = input.next();
                    System.out.print("Specialization: ");
                    String docnewSpecialization = input.next();
                    System.out.print("Address: ");
                    String docnewAddress = input.next();
                    service.updateDoctor(docupdateId, docnewName, docnewPhone, docnewAddress, docnewSpecialization);
                    break;
                case 9:
                    System.out.println("Enter ID of doctor to find:");
                    int docfindId = input.nextInt();
                    System.out.println(service.findDoctorById(docfindId));
                    break;
                case 10:
                    System.out.println("All Appointments: ");
                    for (Doctor doc : service.getAllDoctors())
                        System.out.println(doc);
                    break;
                case 11:
                    System.out.println("Enter the details of the patient:");
                    System.out.print("ID: ");
                    int patientId = input.nextInt();
                    System.out.print("Name: ");
                    String patientName = input.next();
                    System.out.print("Address: ");
                    String patientAddress = input.next();
                    System.out.print("Phone: ");
                    String patientPhone = input.next();
                    System.out.print("Ilness: ");
                    String patientIlness = input.next();
                    System.out.print("Treatment: ");
                    String patientTreatment = input.next();
                    service.addPatient(patientId, patientName, patientAddress, patientPhone, patientIlness, patientTreatment);
                    break;
                case 12:
                    System.out.println("Enter ID of patient to remove:");
                    int patientRemoveId = input.nextInt();
                    service.removePatient(patientRemoveId);
                    break;
                case 13:
                    System.out.println("Enter ID of patient to update: ");
                    int patientUpdateId = input.nextInt();
                    System.out.println("Enter details of patient to update:");
                    System.out.print("Name: ");
                    String patientNewName = input.next();
                    System.out.print("Address: ");
                    String patientNewAddress = input.next();
                    System.out.print("Phone: ");
                    String patientNewPhone = input.next();
                    System.out.print("Ilness: ");
                    String patientNewIlness = input.next();
                    System.out.print("Treatment: ");
                    String patientNewTreatment = input.next();
                    service.updatePatient(patientUpdateId, patientNewName, patientNewAddress, patientNewPhone, patientNewIlness, patientNewTreatment);
                    break;
                case 14:
                    System.out.println("Enter ID of patient to find:");
                    int patientFindId = input.nextInt();
                    System.out.println(service.findPatientById(patientFindId));
                    break;
                case 15:
                    System.out.println("All Appointments: ");
                    for (Patient patient : service.getAllPatients())
                        System.out.println(patient);
                    break;
                case 16:
                    System.out.println("Enter the patient ID: ");
                    int appointedPatientId = input.nextInt();
                    for (DoctorAppointments appointment: service.getAppointmentsForPatient(appointedPatientId))
                        System.out.println(appointment);
                    break;
                case 17:
                    System.out.println("Enter doctor ID: ");
                    int appointedDoctorId = input.nextInt();
                    for (DoctorAppointments appointment: service.getAppointmentsForDoctor(appointedDoctorId))
                        System.out.println(appointment);
                    break;
                case 18:
                    System.out.println("Enter patient ID: ");
                    int patientIdProblems = input.nextInt();
                    System.out.println(service.getPatientProblems(patientIdProblems));
                    break;
                case 19:
                    System.out.print("Enter patient ID: ");
                    int patientIdPhone = input.nextInt();
                    System.out.println(service.getPatientPhoneNumber(patientIdPhone));
                    break;
                case 20:
                    System.out.println("Enter patient ID: ");
                    int patientIdMeds = input.nextInt();
                    System.out.println(service.getPatientTreatment(patientIdMeds));
                    break;
                default:
                    System.out.println("Invalid choice!");
            }
        }
    }
}
