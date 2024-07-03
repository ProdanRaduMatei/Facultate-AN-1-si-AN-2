package repository;

import org.sqlite.SQLiteDataSource;
import java.sql.*;
import domain.Bus;
import java.sql.SQLException;
import java.util.ArrayList;

public class Repository {
    private static final String JDBC_URL = "jdbc:sqlite:data/test_db.db";

    private ArrayList<Bus> elems = new ArrayList<Bus>();
    private static Connection conn = null;
    private String tableName;

    public Repository(String tableName) {
        this.tableName = tableName;
    }

    public static Connection getConnection() {
        if (conn == null)
            openConnection();
        return conn;
    }

    private static void openConnection() {
        try {
            SQLiteDataSource ds = new SQLiteDataSource();
            ds.setUrl(JDBC_URL);
            if (conn == null || conn.isClosed())
                conn = ds.getConnection();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    private void getData() {
        try {
            openConnection();
            String selectString = "SELECT * FROM " + tableName + ";";
            try (Statement statement = conn.createStatement();
                 ResultSet resultSet = statement.executeQuery(selectString)) {
                while (resultSet.next()) {
                    Integer id = resultSet.getInt("id");
                    String sourceCity = resultSet.getString("sourceCity");
                    String destinationCity = resultSet.getString("destinationCity");
                    Integer departureTime = resultSet.getInt("departureTime");
                    Integer arrivalTime = resultSet.getInt("arrivalTime");
                    Integer totalSeats = resultSet.getInt("totalSeats");
                    Integer leftSeats = resultSet.getInt("leftSeats");
                    Integer ticketPrice = resultSet.getInt("ticketPrice");
                    Bus bus = new Bus(id, sourceCity, destinationCity, departureTime, arrivalTime, totalSeats,
                            leftSeats, ticketPrice);
                    elems.add(bus);
                }
            }
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            try {
                closeConnection();
            } catch (Exception e) {
                throw new RuntimeException(e);
            }
        }
    }

    public void add(Bus bus) {
        try {
            openConnection();
            String insertString = "INSERT INTO " + tableName + " VALUES (?, ?, ?, ?, ?, ?, ?, ?)" + ";";
            try (PreparedStatement statement = conn.prepareStatement(insertString)) {
                statement.setInt(1, bus.getId());
                statement.setString(2, bus.getSourceCity());
                statement.setString(3, bus.getDestinationCity());
                statement.setInt(4, bus.getDepartureTime());
                statement.setInt(5, bus.getArrivalTime());
                statement.setInt(6, bus.getTotalSeats());
                statement.setInt(7, bus.getLeftSeats());
                statement.setInt(8, bus.getTicketPrice());
                statement.executeUpdate();
            }
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            try {
                closeConnection();
            } catch (Exception e) {
                throw new RuntimeException(e);
            }
        }
    }

    public void update(Integer id, Bus bus) {
        try {
            openConnection();
            String updateString = "UPDATE " + tableName + " SET sourceCity = ?, destinationCity = ?, departureTime = ?, arrivalTime = ?, totalSeats = ?, leftSeats = ?, ticketPrice = ? WHERE id = " + id + ";";
            try (PreparedStatement statement = conn.prepareStatement(updateString)) {
                statement.setString(1, bus.getSourceCity());
                statement.setString(2, bus.getDestinationCity());
                statement.setInt(3, bus.getDepartureTime());
                statement.setInt(4, bus.getArrivalTime());
                statement.setInt(5, bus.getTotalSeats());
                statement.setInt(6, bus.getLeftSeats());
                statement.setInt(7, bus.getTicketPrice());
                statement.executeUpdate();
            }
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            try {
                closeConnection();
            } catch (Exception e) {
                throw new RuntimeException(e);
            }
        }
    }

    public void delete(Integer id) {
        try {
            openConnection();
            String deleteString = "DELETE FROM " + tableName + " WHERE id = " + id + ";";
            try (PreparedStatement statement = conn.prepareStatement(deleteString)) {
                statement.executeUpdate();
            }
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            try {
                closeConnection();
            } catch (Exception e) {
                throw new RuntimeException(e);
            }
        }
    }

    public Bus findByID(Integer id) {
        try {
            openConnection();
            String selectString = "SELECT * FROM " + tableName + " WHERE id = " + id + ";";
            try (Statement statement = conn.createStatement();
                 ResultSet resultSet = statement.executeQuery(selectString)) {
                if (resultSet.next()) {
                    String sourceCity = resultSet.getString("sourceCity");
                    String destinationCity = resultSet.getString("destinationCity");
                    Integer departureTime = resultSet.getInt("departureTime");
                    Integer arrivalTime = resultSet.getInt("arrivalTime");
                    Integer totalSeats = resultSet.getInt("totalSeats");
                    Integer leftSeats = resultSet.getInt("leftSeats");
                    Integer ticketPrice = resultSet.getInt("ticketPrice");
                    Bus bus = new Bus(id, sourceCity, destinationCity, departureTime, arrivalTime, totalSeats,
                            leftSeats, ticketPrice);
                    return bus;
                }
                throw new RuntimeException("Bus with id " + id + " not found!");
            }
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            try {
                closeConnection();
            } catch (Exception e) {
                throw new RuntimeException(e);
            }
        }
    }

    public ArrayList<Bus> getAll() {
        ArrayList<Bus> buses = new ArrayList<>();
        try {
            openConnection();
            String selectString = "SELECT * FROM " + tableName + ";";
            try (Statement statement = conn.createStatement();
                 ResultSet resultSet = statement.executeQuery(selectString)) {
                while (resultSet.next()) {
                    Integer id = resultSet.getInt("id");
                    String sourceCity = resultSet.getString("sourceCity");
                    String destinationCity = resultSet.getString("destinationCity");
                    Integer departureTime = resultSet.getInt("departureTime");
                    Integer arrivalTime = resultSet.getInt("arrivalTime");
                    Integer totalSeats = resultSet.getInt("totalSeats");
                    Integer leftSeats = resultSet.getInt("leftSeats");
                    Integer ticketPrice = resultSet.getInt("ticketPrice");
                    Bus bus = new Bus(id, sourceCity, destinationCity, departureTime, arrivalTime, totalSeats,
                            leftSeats, ticketPrice);
                    buses.add(bus);
                }
                return buses;
            }
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            try {
                closeConnection();
            } catch (Exception e) {
                throw new RuntimeException(e);
            }
        }
    }

    private static void closeConnection() {
        try {
            conn.close();
            conn = null;
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
