package repository;

import domain.Doctor;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

public class DoctorDatabaseRepository extends DatabaseRepository<Doctor, Integer> {
    public DoctorDatabaseRepository(String tableName) {
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
                    String specialization = resultSet.getString("specialization");
                    Doctor doctor = new Doctor(id, name, specialization, address, phone);
                    elems.put(id, doctor);
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
    public void add(Doctor doctor) {
        try {
            openConnection();
            String insertString = "INSERT INTO " + tableName + " VALUES (?, ?, ?, ?, ?)" + ";";
            try (PreparedStatement statement = connection.prepareStatement(insertString)) {
                statement.setInt(1, doctor.getId());
                statement.setString(2, doctor.getName());
                statement.setString(3, doctor.getPhone());
                statement.setString(4, doctor.getAddress());
                statement.setString(5, doctor.getSpecialization());
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
    public void update(Integer id, Doctor doctor) {
        try {
            openConnection();
            String updateString = "UPDATE " + tableName + " SET name = ?, phone = ?, address = ?, specialization = ? WHERE id =" + id + ";";
            try (PreparedStatement statement = connection.prepareStatement(updateString)) {
                statement.setString(1, doctor.getName());
                statement.setString(2, doctor.getPhone());
                statement.setString(3, doctor.getAddress());
                statement.setString(4, doctor.getSpecialization());
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
    public Doctor findByID(Integer id) {
        try {
            openConnection();
            String selectString = "SELECT * FROM " + tableName + " WHERE id=" + id + ";";
            try (PreparedStatement statement = connection.prepareStatement(selectString)) {
                statement.setInt(1, id);
                ResultSet resultSet = statement.executeQuery();
                if (resultSet.next()) {
                    Integer dbId = resultSet.getInt("id");
                    String name = resultSet.getString("name");
                    String phone = resultSet.getString("phone");
                    String address = resultSet.getString("address");
                    String specialization = resultSet.getString("specialization");
                    Doctor doctor = new Doctor(dbId, name, specialization, address, phone);
                    return doctor;
                }
                throw new RuntimeException("No doctor with id " + id + " found!");
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
    public ArrayList<Doctor> getAll() {
        ArrayList<Doctor> doctors = new ArrayList<>();
        try {
            openConnection();
            String selectString = "SELECT * FROM " + tableName;
            try (PreparedStatement statement = connection.prepareStatement(selectString)) {
                ResultSet resultSet = statement.executeQuery();
                while (resultSet.next()) {
                    Integer id = resultSet.getInt("id");
                    String name = resultSet.getString("name");
                    String phone = resultSet.getString("phone");
                    String address = resultSet.getString("address");
                    String specialization = resultSet.getString("specialization");
                    doctors.add(new Doctor(id, name, specialization, address, phone));
                }
            }
            return doctors;
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
