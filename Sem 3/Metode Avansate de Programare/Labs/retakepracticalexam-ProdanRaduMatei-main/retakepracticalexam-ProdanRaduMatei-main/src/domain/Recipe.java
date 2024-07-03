package domain;

public class Recipe {
    private String name, ingredients;
    private int cookingTime;

    public Recipe() {
        this.name = "";
        this.ingredients = "";
        this.cookingTime = 0;
    }

    public Recipe(String name, int cookingTime, String ingredients) {
        this.name = name;
        this.ingredients = ingredients;
        this.cookingTime = cookingTime;
    }

    public String getName() {
        return name;
    }

    public String getIngredients() {
        return ingredients;
    }

    public int getCookingTime() {
        return cookingTime;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setIngredients(String ingredients) {
        this.ingredients = ingredients;
    }

    public void setCookingTime(int cookingTime) {
        this.cookingTime = cookingTime;
    }

    @Override
    public String toString() {
        return "Recipe{" +
                "name='" + name + '\'' +
                ", ingredients='" + ingredients + '\'' +
                ", cookingTime=" + cookingTime +
                '}';
    }
}
