package domain;

import java.io.Serializable;

public class Vehicle implements Identifiable<Integer>, Serializable {
    private Integer id;
    private String name;
    private String type;
    private String color;
    private Integer year;
    private Integer price;
    private Integer mileage;

    private boolean isRented = false;

    public Vehicle(Integer id, String name, String type, String color, Integer year, Integer price, Integer mileage) {
        this.id = id;
        this.name = name;
        this.type = type;
        this.color = color;
        this.year = year;
        this.price = price;
        this.mileage = mileage;
    }

    @Override
    public Integer getId() {
        return id;
    }

    @Override
    public void setId(Integer id) {
        this.id = id;
    }

    public String printVehicle(){
        return "Vehicle{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", type='" + type + '\'' +
                ", color='" + color + '\'' +
                ", year=" + year +
                ", price=" + price +
                ", mileage=" + mileage +
                '}';
    }

    public String getName() {
        return name;
    }

    public String getType() {
        return type;
    }

    public String getColor() {
        return color;
    }

    public Integer getYear() {
        return year;
    }

    public Integer getPrice() {
        return price;
    }

    public Integer getMileage() {
        return mileage;
    }

    public boolean getIsRented() {
        return isRented;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setType(String type) {
        this.type = type;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public void setYear(Integer year) {
        this.year = year;
    }

    public void setPrice(Integer price) {
        this.price = price;
    }

    public void setMileage(Integer mileage) {
        this.mileage = mileage;
    }

    public void setIsRented(boolean isRented) {
        this.isRented = isRented;
    }
}


