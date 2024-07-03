package org.project;

import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.text.Text;
import org.project.services.Services;

public class Controller {
        @FXML
        private TextField appointmentIdField;

        @FXML
        private TextField appointmentDoctorIdField;

        @FXML
        private TextField appointmentPatientIdField;

        @FXML
        private TextField appointmentSpecializationField;

        @FXML
        private TextField appointmentDateField;

        @FXML
        private Button addAppointmentButton;

        @FXML
        private Button updateAppointmentButton;

        @FXML
        private Button deleteAppointmentButton;

        @FXML
        private Button getAllAppointmentsButton;

        @FXML
        private TextField doctorIdField;

        @FXML
        private TextField doctorNameField;

        @FXML
        private TextField doctorPhoneField;

        @FXML
        private TextField doctorAddressField;

        @FXML
        private TextField doctorSpecialtyField;

        @FXML
        private Button addDoctorButton;

        @FXML
        private Button updateDoctorButton;

        @FXML
        private Button deleteDoctorButton;

        @FXML
        private Button getAllDoctorsButton;

        @FXML
        private TextField patientIdField;

        @FXML
        private TextField patientNameField;

        @FXML
        private TextField patientPhoneField;

        @FXML
        private TextField patientAddressField;

        @FXML
        private TextField patientIllnessField;

        @FXML
        private TextField patientTreatmentField;

        @FXML
        private Button addPatientButton;

        @FXML
        private Button updatePatientButton;

        @FXML
        private Button deletePatientButton;

        @FXML
        private Button getAllPatientsButton;

        private Services services;

        public void setServices(Services services) {
            this.services = services;
        }

        private void clearAppointmentFields() {
            appointmentIdField.clear();
            appointmentDoctorIdField.clear();
            appointmentPatientIdField.clear();
            appointmentSpecializationField.clear();
            appointmentDateField.clear();
        }

        private void clearDoctorFields() {
            doctorIdField.clear();
            doctorNameField.clear();
            doctorPhoneField.clear();
            doctorAddressField.clear();
            doctorSpecialtyField.clear();
        }

        private void clearPatientFields() {
            patientIdField.clear();
            patientNameField.clear();
            patientPhoneField.clear();
            patientAddressField.clear();
            patientIllnessField.clear();
            patientTreatmentField.clear();
        }

        @FXML
        public void initialize() {
            addAppointmentButton.setOnAction(event -> {
                services.addAppointment(
                        Integer.parseInt(appointmentIdField.getText()),
                        Integer.parseInt(appointmentDoctorIdField.getText()),
                        Integer.parseInt(appointmentPatientIdField.getText()),
                        appointmentSpecializationField.getText(),
                        appointmentDateField.getText()
                );
                clearAppointmentFields();
            });

            addDoctorButton.setOnAction(event -> {
                services.addDoctor(
                        Integer.parseInt(doctorIdField.getText()),
                        doctorNameField.getText(),
                        doctorPhoneField.getText(),
                        doctorAddressField.getText(),
                        doctorSpecialtyField.getText()
                );
                clearDoctorFields();
            });

            addPatientButton.setOnAction(event -> {
                services.addPatient(
                        Integer.parseInt(patientIdField.getText()),
                        patientNameField.getText(),
                        patientPhoneField.getText(),
                        patientAddressField.getText(),
                        patientIllnessField.getText(),
                        patientTreatmentField.getText()
                );
                clearPatientFields();
            });

            updateAppointmentButton.setOnAction(event -> {
                services.updateAppointment(
                        Integer.parseInt(appointmentIdField.getText()),
                        Integer.parseInt(appointmentDoctorIdField.getText()),
                        Integer.parseInt(appointmentPatientIdField.getText()),
                        appointmentSpecializationField.getText(),
                        appointmentDateField.getText()
                );
                clearAppointmentFields();
            });

            updateDoctorButton.setOnAction(event -> {
                services.updateDoctor(
                        Integer.parseInt(doctorIdField.getText()),
                        doctorNameField.getText(),
                        doctorPhoneField.getText(),
                        doctorAddressField.getText(),
                        doctorSpecialtyField.getText()
                );
                clearDoctorFields();
            });

            updatePatientButton.setOnAction(event -> {
                services.updatePatient(
                        Integer.parseInt(patientIdField.getText()),
                        patientNameField.getText(),
                        patientPhoneField.getText(),
                        patientAddressField.getText(),
                        patientIllnessField.getText(),
                        patientTreatmentField.getText()
                );
                clearPatientFields();
            });

            deleteAppointmentButton.setOnAction(event -> {
                services.removeAppointment(Integer.parseInt(appointmentIdField.getText()));
                clearAppointmentFields();
            });

            deleteDoctorButton.setOnAction(event -> {
                services.removeDoctor(Integer.parseInt(doctorIdField.getText()));
                clearDoctorFields();
            });

            deletePatientButton.setOnAction(event -> {
                services.removePatient(
                        Integer.parseInt(patientIdField.getText())
                );
                clearPatientFields();
            });

            getAllAppointmentsButton.setOnAction(event -> {
                StringBuilder result = new StringBuilder();
                for (var appointment : services.getAllAppointments())
                    result.append(appointment.toString()).append("/n");
                Text text = new Text(result.toString());
                text.setWrappingWidth(500);
                text.setLineSpacing(5);
                text.setStyle("-fx-font-size: 14px;");
            });

            getAllDoctorsButton.setOnAction(event -> {
                StringBuilder result = new StringBuilder();
                for(var doctor : services.getAllDoctors())
                    result.append(doctor.toString()).append("\n");
                Text text = new Text(result.toString());
                text.setWrappingWidth(500);
                text.setLineSpacing(5);
                text.setStyle("-fx-font-size: 14px;");
            });

            getAllPatientsButton.setOnAction(event -> {
                StringBuilder result = new StringBuilder();
                for(var patient : services.getAllPatients())
                    result.append(patient.toString()).append("\n");
                Text text = new Text(result.toString());
                text.setWrappingWidth(500);
                text.setLineSpacing(5);
                text.setStyle("-fx-font-size: 14px;");
            });
        }
}