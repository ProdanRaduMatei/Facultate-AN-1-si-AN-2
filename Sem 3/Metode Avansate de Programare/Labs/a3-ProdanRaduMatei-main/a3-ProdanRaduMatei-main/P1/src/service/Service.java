package service;

import domain.Car;
import repository.CarRepo;

import javax.security.auth.login.LoginException;
import java.util.NoSuchElementException;

public class Service {
    //the id of a free car will be considered as the id of the reservation when that car is used
    private CarRepo freeCars = new CarRepo();
    private int validCarId = 0;

    private void initCars() {

        Car car1 = new Car(validCarId++,"Mazda", "Miata NA", 1998, 123400, 250);
        Car car2 = new Car(validCarId++,"Mazda", "Rx-7 FC Turbo", 1990, 84203, 550);
        Car car3 = new Car(validCarId++,"BMW", "E30", 1987, 941478, 300);
        Car car4 = new Car(validCarId++,"Toyota", "MR2", 1986, 441478, 400);
        Car car5 = new Car(validCarId++,"Toyota", "Trueno AE86", 1985, 1941478, 700);
        Car car6 = new Car(validCarId++,"Dacia", "1300", 1990, 1041786, 50);
        Car car7 = new Car(validCarId++,"Dacia", "Logan", 2008, 41786, 600);
        Car car8 = new Car(validCarId++,"Honda", "S200", 2004, 21786, 900);
        Car car9 = new Car(validCarId++,"Subaru", "Impreza WRX STI", 2004, 21786, 1000);
        Car car10 = new Car(validCarId++,"Mitsubishi", "Lancer Evo IX ", 2006, 2186, 1005);


        freeCars.add(car1);
        freeCars.add(car2);
        freeCars.add(car3);
        freeCars.add(car4);
        freeCars.add(car5);
        freeCars.add(car6);
        freeCars.add(car7);
        freeCars.add(car8);
        freeCars.add(car9);
        freeCars.add(car10);
    }

    private void initRepos() throws LoginException {
        initCars();
    }

    public Service() throws LoginException {
        initRepos();
    }

    public Iterable<Car> freeCars()
    {
        return freeCars.getAll();
    }
    public Car addNewFreeCar(String brand, String model, int year, float mileage, float cost)
    {
        Car car = new Car(validCarId++,brand, model, year, mileage, cost);
        freeCars.add(car);
        return car;
    }

    public Car removeFreeCar(int carId)
            throws NoSuchElementException
    {
        Car car = freeCars.findByID(carId);
        if (car == null)
            throw new NoSuchElementException("There is no free car by that id!");
        else
            return freeCars.delete(carId);
    }

    public Car getFreeCarById(int carId)
            throws NoSuchElementException
    {
        Car car = freeCars.findByID(carId);
        if (car == null)
            throw new NoSuchElementException("There is no free car by that id!");
        else
            return car;
    }

    public int noOfFreeCars()
    {
        return freeCars.size();
    }

}
