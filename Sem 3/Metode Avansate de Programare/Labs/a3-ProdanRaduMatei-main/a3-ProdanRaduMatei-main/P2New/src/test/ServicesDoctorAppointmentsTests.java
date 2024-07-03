package test;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import services.Services;
import domain.DoctorAppointments;

public class ServicesDoctorAppointmentsTests {
    @Test
    void testAddAppointment() {
        //Arrange
        Services service = new Services();
        DoctorAppointments app = new DoctorAppointments(1, "John Doe", "Cardiology", "Cluj", "0744123456", true, "2022-02-15");
        service.addAppointment(1, "John Doe", "Cardiology", "Cluj", "0744123456", true, "2022-02-15");
        DoctorAppointments addedApp = service.findAppointmentsById(1);
        assertEquals(app, addedApp);
    }

    @Test
    void testDeleteAppointment() {
        Services service = new Services();
        service.addAppointment(1, "John Doe", "Cardiology", "Cluj", "0744123456", true, "2022-02-15");
        service.removeAppointment(1);
        assertThrows(RuntimeException.class, () -> service.findAppointmentsById(1));
    }

    @Test
    void testUpdateAppointment() {
        Services service = new Services();
        service.addAppointment(1, "John Doe", "Cardiology", "Cluj", "0744123456", true, "2022-02-15");
        service.updateAppointment(1, "Jane Doe", "Neurology", "Bucharest", "0712345678", false, "2023-01-15");
        DoctorAppointments updatedApp = new DoctorAppointments(1, "Jane Doe", "Neurology", "Bucharest", "0712345678", false, "2023-01-15");
        DoctorAppointments foundApp = service.findAppointmentsById(1);
        assertEquals(updatedApp, foundApp);
    }

    @Test
    void testFindAppointmentById() {
        Services service = new Services();
        DoctorAppointments app = new DoctorAppointments(1, "John Doe", "Cardiology", "Cluj", "0744123456", true, "2022-02-15");
        service.addAppointment(1, "John Doe", "Cardiology", "Cluj", "0744123456", true, "2022-02-15");
        DoctorAppointments foundApp = service.findAppointmentsById(1);
        assertEquals(app, foundApp);
    }

    @Test
    void testFindAllAppointments() {
        Services service = new Services();
        DoctorAppointments app1 = new DoctorAppointments(1, "John Doe", "Cardiology", "Cluj", "0744123456", true, "2022-02-15");
        DoctorAppointments app2 = new DoctorAppointments(2, "Jane Doe", "Neurology", "Bucharest", "0723456789", false, "2023-01-15");

        service.addAppointment(1, "John Doe", "Cardiology", "Cluj", "0744123456", true, "2022-02-15");
        service.addAppointment(2, "Jane Doe", "Neurology", "Bucharest", "0723456789", false, "2023-01-15");
        java.util.List<DoctorAppointments> allApps = service.getAllAppointments();
        for (DoctorAppointments app : allApps) {
            if(app.getId() == 1) {
                assertEquals(app1, app);
            } else if (app.getId() == 2) {
                assertEquals(app2, app);
            }
        }
    }
}
