package main;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;
import ui.*;

public class Main extends Application {

    @Override
    public void start(Stage primaryStage) throws Exception{
        // first window
        FXMLLoader loader = new FXMLLoader(getClass().getResource("/ui/pizza_app.fxml"));

        Controller controller = new Controller();
        loader.setController(controller);
        Parent root = (Parent)loader.load();

        primaryStage.setTitle("Pizza Place");
        primaryStage.setScene(new Scene(root, 600, 500));
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
