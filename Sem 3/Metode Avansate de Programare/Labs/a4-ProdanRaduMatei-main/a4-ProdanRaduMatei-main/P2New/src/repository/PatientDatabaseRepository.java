package repository;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

import domain.Patient;

public class PatientDatabaseRepository extends DatabaseRepository<Patient, Integer> {
    public PatientDatabaseRepository(String tableName) {
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
                    String name = resultSet.getString("name");
                    String phone = resultSet.getString("phone");
                    String address = resultSet.getString("address");
                    String illness = resultSet.getString("illness");
                    String treatment = resultSet.getString("treatment");
                    Patient patient = new Patient(id, name, phone, address, illness, treatment);
                    elems.put(id, patient);
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
    public void add(Patient patient) {
        try {
            openConnection();
            String insertString = "INSERT INTO " + tableName + " VALUES (?, ?, ?, ?, ?, ?)";
            try (PreparedStatement statement = connection.prepareStatement(insertString)) {
                statement.setInt(1, patient.getId());
                statement.setString(2, patient.getName());
                statement.setString(3, patient.getPhone());
                statement.setString(4, patient.getAddress());
                statement.setString(5, patient.getIllness());
                statement.setString(6, patient.getTreatment());
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
    public void update(Integer id, Patient patient) {
        try {
            openConnection();
            String updateString = "UPDATE " + tableName + " SET name=?, phone=?, address=?, illness=?, treatment=? WHERE id=" + id + ";";
            try (PreparedStatement statement = connection.prepareStatement(updateString)) {
                statement.setString(1, patient.getName());
                statement.setString(2, patient.getPhone());
                statement.setString(3, patient.getAddress());
                statement.setString(4, patient.getIllness());
                statement.setString(5, patient.getTreatment());
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
    public Patient findByID(Integer id) {
        try {
            openConnection();
            String selectString = "SELECT * FROM " + tableName + " WHERE id=" + id + ";";
            try (PreparedStatement statement = connection.prepareStatement(selectString)) {
                statement.setInt(1, id);
                ResultSet resultSet = statement.executeQuery();
                if(resultSet.next()) {
                    Integer patientId = resultSet.getInt("id");
                    String name = resultSet.getString("name");
                    String phone = resultSet.getString("phone");
                    String address = resultSet.getString("address");
                    String illness = resultSet.getString("illness");
                    String treatment = resultSet.getString("treatment");
                    return new Patient(patientId, name, phone, address, illness, treatment);
                }
                throw new RuntimeException("No patient found with id " + id + " found");
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
    public ArrayList<Patient> getAll() {
        ArrayList<Patient> patients = new ArrayList<>();
        try {
            openConnection();
            String selectString = "SELECT * FROM " + tableName + ";";
            try (PreparedStatement statement = connection.prepareStatement(selectString)) {
                ResultSet resultSet = statement.executeQuery();
                while (resultSet.next()) {
                    Integer id = resultSet.getInt("id");
                    String name = resultSet.getString("name");
                    String phone = resultSet.getString("phone");
                    String address = resultSet.getString("address");
                    String illness = resultSet.getString("illness");
                    String treatment = resultSet.getString("treatment");
                    patients.add(new Patient(id, name, phone, address, illness, treatment));
                }
                return patients;
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
