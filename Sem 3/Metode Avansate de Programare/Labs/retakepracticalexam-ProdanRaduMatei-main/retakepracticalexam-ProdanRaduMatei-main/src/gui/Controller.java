package gui;

import javafx.collections.ObservableList;
import javafx.scene.control.TextField;
import org.w3c.dom.Text;
import service.Service;
import domain.Recipe;
import javafx.collections.FXCollections;
import javafx.fxml.FXML;
import javafx.scene.control.ListView;
import javafx.scene.control.Button;


public class Controller {
    private Service service;

    public Controller(Service service) {
        this.service = service;
    }

    //1.
    private ObservableList<Recipe> recipeList = FXCollections.observableArrayList();

    @FXML
    private ListView<Recipe> recipeListView = new ListView<>();

//    2.
    @FXML
    private ObservableList<Recipe> recipeList2 = FXCollections.observableArrayList();

    @FXML
    private ListView<Recipe> recipeListView2 = new ListView<>();

    @FXML
    private TextField selectedTime = new TextField();

    @FXML
    private TextField selectedIngredient = new TextField();

    @FXML
    private Button searchButton = new Button();

//   3.
    @FXML
    private TextField recipeName = new TextField();

    @FXML
    private TextField cookingTime = new TextField();

    @FXML
    private TextField ingredients = new TextField();

    @FXML
    private ObservableList<Recipe> recipeList3 = FXCollections.observableArrayList();

    @FXML
    private ListView<Recipe> recipeListView3 = new ListView<>();

    public void initialize() {
//        1.
        recipeList.addAll(service.getAll());
        recipeListView.setItems(recipeList);

//        2.
        searchButton.setOnAction(actionEvent -> {
            recipeList2.clear();
            recipeList2.addAll(service.Filter(Integer.parseInt(selectedTime.getText()), selectedIngredient.getText()));
            recipeListView2.setItems(recipeList2);
        });

//        3.
        recipeName.setOnAction(actionEvent -> {
            Recipe recipe = new Recipe();
            recipe.setName(recipeName.getText());
            recipe.setCookingTime(Integer.parseInt(cookingTime.getText()));
            recipe.setIngredients(ingredients.getText());
            service.addRecipe(recipe);
            recipeList3.clear();
            recipeList3.addAll(service.getAll());
            recipeListView3.setItems(recipeList);
        });
    }
}
