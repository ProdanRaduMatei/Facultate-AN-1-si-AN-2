module com.example.seminar7 {
    requires javafx.controls;
    requires javafx.fxml;

    opens ui to javafx.fxml;
    exports ui;
    exports main;
}