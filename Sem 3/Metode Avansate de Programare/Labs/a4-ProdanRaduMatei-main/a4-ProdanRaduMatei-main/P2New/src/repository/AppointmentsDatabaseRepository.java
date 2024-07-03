package repository;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

import domain.DoctorAppointments;

public class AppointmentsDatabaseRepository extends DatabaseRepository< DoctorAppointments, Integer> {
    public AppointmentsDatabaseRepository(String tableName) {
        super(tableName);
        getData();
    }

    @Override
    public void getData() {
        try {
            openConnection();
            String selectString = "SELECT * FROM " + tableName + ";";
            try (PreparedStatement statement = connection.prepareStatement(selectString)) {
                ResultSet resultSet = statement.executeQuery();
                while (resultSet.next()) {
                    Integer id = resultSet.getInt("id");
                    Integer doctorId = resultSet.getInt("doctor_id");
                    Integer patientId = resultSet.getInt("patient_id");
                    String specialization = resultSet.getString("specialization");
                    String appointedTime = resultSet.getString("appointed_time");
                    DoctorAppointments doctorAppointment = new DoctorAppointments(
                            id, doctorId, patientId, specialization, appointedTime);
                    elems.put(id, doctorAppointment);
                }
        }
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            try {
                closeConnection();
            } catch (SQLException e) {
                throw new RuntimeException(e);
            }
        }
    }

    @Override
    public void add(DoctorAppointments appointment) {
        try {
            openConnection();
            String insertString = "INSERT INTO " + tableName + " VALUES (?, ?, ?, ?, ?)" + ";";
            try (PreparedStatement statement = connection.prepareStatement(insertString)) {
                statement.setInt(1, appointment.getId());
                statement.setInt(2, appointment.getDoctorId());
                statement.setInt(3, appointment.getPatientId());
                statement.setString(4, appointment.getSpecialization());
                statement.setString(5, appointment.getAppointedTime());
                statement.executeUpdate();
            }
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            try {
                closeConnection();
            } catch (SQLException e) {
                throw new RuntimeException(e);
            }
        }
    }

    @Override
    public void update(Integer id, DoctorAppointments appointment) {
        try {
            openConnection();
            String updateString = "UPDATE " + tableName + " SET doctor_id=?, patient_id=?, specialization=?, appointed_time=? WHERE id=" + id + ";";
            try (PreparedStatement statement = connection.prepareStatement(updateString)) {
                statement.setInt(1, appointment.getDoctorId());
                statement.setInt(2, appointment.getPatientId());
                statement.setString(3, appointment.getSpecialization());
                statement.setString(4, appointment.getAppointedTime());
                statement.executeUpdate();
            }
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            try {
                closeConnection();
            } catch (SQLException e) {
                throw new RuntimeException(e);
            }
        }
    }

    @Override
    public void delete(Integer id) {
        try {
            openConnection();
            String deleteString = "DELETE FROM " + tableName + " WHERE id=" + id + ";";
            try (PreparedStatement statement = connection.prepareStatement(deleteString)) {
                statement.setInt(1, id);
                statement.executeUpdate();
            }
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            try {
                closeConnection();
            } catch (SQLException e) {
                throw new RuntimeException(e);
            }
        }
    }

    @Override
    public DoctorAppointments findByID(Integer id) {
        try {
            openConnection();
            String selectString = "SELECT * FROM " + tableName + " WHERE id=" + id + ";";
            try (PreparedStatement statement = connection.prepareStatement(selectString)) {
                statement.setInt(1, id);
                ResultSet resultSet = statement.executeQuery();
                if (resultSet.next()) {
                    Integer doctorId = resultSet.getInt("doctor_id");
                    Integer patientId = resultSet.getInt("patient_id");
                    String specialization = resultSet.getString("specialization");
                    String appointedTime = resultSet.getString("appointed_time");
                    return new DoctorAppointments(id, doctorId, patientId, specialization, appointedTime);
                }
                throw new RuntimeException("No appointment with id " + id + " found!");
            }
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            try {
                closeConnection();
            } catch (SQLException e) {
                throw new RuntimeException(e);
            }
        }
    }


    @Override
    public ArrayList<DoctorAppointments> getAll() {
        ArrayList<DoctorAppointments> appointments = new ArrayList<>();
        try {
            openConnection();
            String selectString = "SELECT * FROM " + tableName + ";";
            try (PreparedStatement statement = connection.prepareStatement(selectString)) {
                ResultSet resultSet = statement.executeQuery();
                while (resultSet.next()) {
                    Integer id = resultSet.getInt("id");
                    Integer doctorId = resultSet.getInt("doctor_id");
                    Integer patientId = resultSet.getInt("patient_id");
                    String specialization = resultSet.getString("specialization");
                    String appointedTime = resultSet.getString("appointed_time");
                    appointments.add(new DoctorAppointments(
                            id, doctorId, patientId, specialization, appointedTime));
                }
                return appointments;
            }
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            try {
                closeConnection();
            } catch (SQLException e) {
                throw new RuntimeException(e);
            }
        }
    }

}
