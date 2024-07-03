package test;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import domain.DoctorAppointments;
import repository.AppointmentsRepository;

public class RepositoryDoctorAppointmentsTests {
    @Test
    void testAdd() {
        AppointmentsRepository repo = new AppointmentsRepository();
        DoctorAppointments da = new DoctorAppointments(1, "John Doe", "Cardiology", "Cluj", "0712345678", false, "2023-01-01");
        repo.add(da);
        for (DoctorAppointments daAdded : repo.getAll())
            assertEquals(da, daAdded);
    }

    @Test
    void testUpdate() {
        AppointmentsRepository repo = new AppointmentsRepository();
        DoctorAppointments da = new DoctorAppointments(1, "John Doe", "Cardiology", "Cluj", "0712345678", false, "2023-01-01");
        repo.add(da);

        DoctorAppointments daUpdated = new DoctorAppointments(1, "Jane Doe", "Oncology", "Bucharest", "0723456789", true, "2023-01-15");
        repo.update(1, daUpdated);

        DoctorAppointments daFromRepo = repo.findByID(1);
        assertEquals(daUpdated, daFromRepo);
    }

    @Test
    void testDelete() {
        AppointmentsRepository repo = new AppointmentsRepository();
        DoctorAppointments da = new DoctorAppointments(1, "John Doe", "Cardiology", "Cluj", "0712345678", false, "2023-01-01");
        repo.add(da);
        repo.delete(1);
        assertThrows(RuntimeException.class, () -> repo.findByID(1));
    }

    @Test
    void testFindByID() {
        AppointmentsRepository repo = new AppointmentsRepository();
        DoctorAppointments da = new DoctorAppointments(1, "John Doe", "Cardiology", "Cluj", "0712345678", false, "2023-01-01");
        repo.add(da);
        DoctorAppointments daFromRepo = repo.findByID(1);
        assertEquals(da, daFromRepo);
    }

    @Test
    void testFindAll() {
        AppointmentsRepository repo = new AppointmentsRepository();
        DoctorAppointments da1 = new DoctorAppointments(1, "John Doe", "Cardiology", "Cluj", "0712345678", false, "2023-01-01");
        repo.add(da1);

        DoctorAppointments da2 = new DoctorAppointments(2, "Jane Doe", "Oncology", "Bucharest", "0723456789", true, "2023-01-15");
        repo.add(da2);

        for (DoctorAppointments da : repo.getAll()) {
            if(da.getId() == 1)
                assertEquals(da1, da);
            else if(da.getId() == 2)
                assertEquals(da2, da);
            else
                fail("Invalid appointment!");
        }
    }
}
