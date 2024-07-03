package test;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import domain.DoctorAppointments;

public class DomainDoctorAppointmentsTests {
    @Test
    void testId() {
        DoctorAppointments da = new DoctorAppointments(1, "John Doe", "Cardiology", "Cluj", "0712345678", false, "2023-01-01");
        assertEquals(1, da.getId());
    }

    @Test
    void testName() {
        DoctorAppointments da = new DoctorAppointments(1, "John Doe", "Cardiology", "Cluj", "0712345678", false, "2023-01-01");
        assertEquals("John Doe", da.getName());
    }


    @Test
    void testSpecialty() {
        DoctorAppointments da = new DoctorAppointments(1, "John Doe", "Cardiology", "Cluj", "0712345678", false, "2023-01-01");
        assertEquals("Cardiology", da.getSpecialization());
    }

    @Test
    void testAddress() {
        DoctorAppointments da = new DoctorAppointments(1, "John Doe", "Cardiology", "Cluj", "0712345678", false, "2023-01-01");
        assertEquals("Cluj", da.getAddress());
    }

    @Test
    void testPhone() {
        DoctorAppointments da = new DoctorAppointments(1, "John Doe", "Cardiology", "Cluj", "0712345678", false, "2023-01-01");
        assertEquals("0712345678", da.getPhone());
    }

    @Test
    void testisAppointed() {
        DoctorAppointments da = new DoctorAppointments(1, "John Doe", "Cardiology", "Cluj", "0712345678", false, "2023-01-01");
        assertEquals(false, da.getIsAppointed());
    }

    @Test
    void testDate() {
        DoctorAppointments da = new DoctorAppointments(1, "John Doe", "Cardiology", "Cluj", "0712345678", false, "2023-01-01");
        assertEquals("2023-01-01", da.getAppointedTime());
    }
}