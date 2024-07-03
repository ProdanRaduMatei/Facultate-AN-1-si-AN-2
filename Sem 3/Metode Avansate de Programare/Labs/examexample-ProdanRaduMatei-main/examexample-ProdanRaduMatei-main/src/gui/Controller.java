package gui;

import javafx.scene.control.ListView;
import javafx.scene.control.TextField;
import service.Service;
import domain.Bus;
import javafx.collections.ObservableList;
import javafx.collections.FXCollections;
import javafx.scene.control.Button;
import java.util.List;
import javafx.fxml.FXML;

public class Controller {
    private Service service;

    public Controller(Service service) {
        this.service = service;
    }

    private ObservableList<Bus> busList = FXCollections.observableArrayList();

    @FXML
    private ListView<Bus> busesListView;

    @FXML
    private TextField departureCityTextField;

    @FXML
    private TextField departureTimeTextField;

    @FXML
    private Button searchButton;

    @FXML
    public void initialize() {
        searchButton.setOnAction(actionEvent -> {
            List<Bus> buses = service.getBusesByCityAndTime(departureCityTextField.getText(),
                    Integer.valueOf(departureTimeTextField.getText()));
            busList = FXCollections.observableList(buses);
            busesListView.setItems(busList);
        });
    }
}
