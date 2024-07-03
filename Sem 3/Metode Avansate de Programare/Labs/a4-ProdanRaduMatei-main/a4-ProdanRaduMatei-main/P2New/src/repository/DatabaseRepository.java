package repository;

import domain.Identifiable;
import org.sqlite.SQLiteDataSource;

import java.sql.Connection;
import java.sql.SQLException;

public abstract class DatabaseRepository<T extends Identifiable<ID>, ID> extends MemoryRepository<ID, T> {
    protected final String url = "jdbc:sqlite:/Users/matei/Desktop/AN2/Sem 3/Metode Avansate de Programare/Labs/a4-ProdanRaduMatei/P2New/data/test.db";

    protected String tableName;
    protected Connection connection = null;

    public DatabaseRepository(String tableName) {
        this.tableName = tableName;
    }

    public abstract void getData();

    public void openConnection() throws SQLException {
        SQLiteDataSource dataSource = new SQLiteDataSource();
        dataSource.setUrl(url);
        if (connection == null || connection.isClosed()) {
            connection = dataSource.getConnection();
        }
    }

    public void closeConnection() throws SQLException {
        if (connection != null && !connection.isClosed()) {
            connection.close();
        }
    }
}
