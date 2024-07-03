package repository;
import domain.Question;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

import org.sqlite.SQLiteDataSource;

public class QuestionsRepository implements RIdentifiable<Integer, Question> {
    protected final String url = "jdbc:sqlite:/Users/antor/IdeaProjects/PracticMAPTry/src/data/test.db";
    protected String tableName;
    protected Connection conn = null;
    public QuestionsRepository(String tableName) {
        this.tableName = tableName;
    }
    public void openConnection() throws SQLException {
        SQLiteDataSource dataSource = new SQLiteDataSource();
        dataSource.setUrl(url);
        if (conn == null || conn.isClosed())
            conn = dataSource.getConnection();
    }
    public void closeConnection() throws SQLException {
        conn.close();
    }

    public void add

    public void getData() throws SQLException {
        try {
            openConnection();
            String selectString = "SELECT * FROM " + tableName + ";";
            try(PreparedStatement ps = conn.prepareStatement(selectString)) {
                ResultSet resultSet = ps.executeQuery();
                while (resultSet.next()) {
                    int id = resultSet.getInt("id");
                    String text = resultSet.getString("text");
                    String answer = resultSet.getString("answer");
                    int score = resultSet.getInt("score");
                    String usranswr = resultSet.getString("usranswr");
                    Boolean isAnswered = resultSet.getBoolean("isAnswered");
                    Question question = new Question(id, text, answer, score, usranswr, isAnswered);
                    super.add(question);
                }
            } catch (SQLException e) {
                throw new RuntimeException(e);
            }
        }
    }

    @Override
    public void add(Question object) {

    }

    @Override
    public Question delete(Integer integer) {
        return null;
    }

    @Override
    public Question update(Question object) {
        return null;
    }

    @Override
    public Question findById(Integer integer) {
        return null;
    }

    @Override
    public Iterable<Question> getAll() {
        return null;
    }
}
