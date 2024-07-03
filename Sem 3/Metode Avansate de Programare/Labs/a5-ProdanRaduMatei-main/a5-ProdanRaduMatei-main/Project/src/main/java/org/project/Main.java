package org.project;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;
import java.io.IOException;

import org.project.services.Services;

public class Main extends Application {
    @Override
    public void start(Stage stage) throws IOException {
        Services services = new Services();
        FXMLLoader fxmlLoader = new FXMLLoader(Main.class.getResource("controller-view.fxml"));
        Scene scene = new Scene(fxmlLoader.load(), 600, 400);
        Controller controller = fxmlLoader.getController();
        controller.setServices(services);
        stage.setTitle("Appointments!");
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        launch();
    }
}