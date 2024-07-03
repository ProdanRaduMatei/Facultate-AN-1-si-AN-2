package service;
import domain.Recipe;

import repository.Repository;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.stream.Collectors;

public class Service {
    private Repository repo;

    public Service(Repository repo) {
        this.repo = repo;
    }

    public ArrayList<Recipe> getAll() {
        try {
            Connection connection = repo.getConnection();
            String selectString = "SELECT * FROM recipes;";
            try (Statement statement = connection.createStatement();
                 ResultSet resultSet = statement.executeQuery(selectString)) {
                ArrayList<Recipe> recipes = new ArrayList<>();
                while (resultSet.next()) {
                    String name = resultSet.getString("name");
                    Integer cookingTime = resultSet.getInt("cookingTime");
                    String ingredients = resultSet.getString("ingredients");

                    Recipe recipe = new Recipe(name, cookingTime, ingredients);
                    recipes.add(recipe);
                }
                // sort by ascending by name
                recipes.sort((r1, r2) -> r1.getName().compareTo(r2.getName()));
//            System.out.println(recipes);
                return recipes;
            }
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }

    // filter recipes by cooking time and ingredient, java streams
    public ArrayList<Recipe> Filter(int val, String ingredient) {
        ArrayList<Recipe> recipes = new ArrayList<>();
        recipes = getAll();
        return (ArrayList<Recipe>) recipes.stream()
                .filter(r -> r.getCookingTime() <= val)
                .filter(r -> r.getIngredients().contains(ingredient))
                .collect(Collectors.toList());
    }

    // add a recipe to the database
    public void addRecipe(Recipe recipe) {
        try {
            Connection connection = repo.getConnection();
            String insertString = "INSERT INTO recipes (name, cookingTime, ingredients) VALUES ('" + recipe.getName() + "', " + recipe.getCookingTime() + ", '" + recipe.getIngredients() + "');";
            try (Statement statement = connection.createStatement()) {
                statement.executeUpdate(insertString);
            }
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }
}

