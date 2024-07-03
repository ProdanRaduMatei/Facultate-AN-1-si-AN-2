package ui;

import domain.Car;
import service.Service;

import javax.security.auth.login.LoginException;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.NoSuchElementException;

public class Ui {
    private Service service = new Service();
    final private String menuMessage = "Car Rentals:\n" +
                                "0) Exit\n" +
                                "1) View free Cars.\n" +
                                "2) Add free car.\n" +
                                "3) Remove free car.\n" +
                                "4) Update free car.\n";

    public Ui() throws LoginException {
    }
    private Car askForFreeCar() throws IOException, RuntimeException
    {
        if (service.noOfFreeCars() == 0) {
            throw new RuntimeException("No free cars!");
        }

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Car car = null;
        boolean failed;
        do
        {
            try {
                System.out.print("Enter car id:\n>>\t");
                int carId = Integer.parseInt(br.readLine());

                car = service.getFreeCarById(carId);

                failed = false;
            } catch (NoSuchElementException exception) {
                System.out.println("Could not find a free car by that id.");
                failed = true;
            } catch (NumberFormatException exception)
            {
                System.out.println("Could not convert input into integer.");
                failed = true;
            }

        }while (failed);

        return car;
    }

    class PrimitiveCar
    {
        public String brand, model;
        public int year;
        public float mileage, cost;

        public PrimitiveCar() {}
        public PrimitiveCar(String brand, String model, int year, float mileage, float cost) {
            this.brand = brand;
            this.model = model;
            this.year = year;
            this.mileage = mileage;
            this.cost = cost;
        }
    }
    private PrimitiveCar askUserForNewCarData() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        PrimitiveCar car = new PrimitiveCar();

        System.out.print("Enter car brand:\n>>\t");
        car.brand = br.readLine();

        System.out.print("Enter car model:\n>>\t");
        car.model = br.readLine();

        boolean failed;
        do {
            try {
                System.out.print("Enter car year:\n>>\t");
                car.year = Integer.parseInt(br.readLine());

                failed = false;
            } catch (NumberFormatException exception) {
                System.out.println("Could not convert input into integer.");
                failed = true;
            }
        } while (failed);


        do {
            try {
                System.out.print("Enter car mileage:\n>>\t");
                car.mileage = Float.parseFloat(br.readLine());

                failed = false;
            } catch (NumberFormatException exception) {
                System.out.println("Could not convert input into float.");
                failed = true;
            }
        } while (failed);

        do {
            try {
                System.out.print("Enter car cost:\n>>\t");
                car.cost = Float.parseFloat(br.readLine());

                failed = false;
            } catch (NumberFormatException exception) {
                System.out.println("Could not convert input into float.");
                failed = true;
            }
        } while (failed);

        return car;
    }

    
    

    private String viewCars() throws IOException{
        StringBuilder result = new StringBuilder();

        for (Car car : service.freeCars())
            result.append(car.toString()).append(";\n");

        if (result.isEmpty())
            return  "There are no free cars!";
        else
            return result.toString();
    }
    private String addCar() throws IOException{
        PrimitiveCar primitiveCar = askUserForNewCarData();
        Car car = service.addNewFreeCar(primitiveCar.brand, primitiveCar.model, primitiveCar.year,
                                        primitiveCar.mileage, primitiveCar.cost);

        return "Added " + car.toString() + ";";
    }

    private String removeCar(){
        try {
            Car chosenCar = askForFreeCar();

            service.removeFreeCar(chosenCar.getId());
            return "Removed " + chosenCar.toString();
        } catch (Exception exception)
        {
            return exception.getMessage();
        }

    }

    private String updateCar() throws IOException{
        try {
            Car chosenCar = askForFreeCar();
            String oldCarStr = chosenCar.toString();

            PrimitiveCar updatedCar = askUserForNewCarData();
            chosenCar.setBrand(updatedCar.brand);
            chosenCar.setModel(updatedCar.model);
            chosenCar.setYear(updatedCar.year);
            chosenCar.setMileage(updatedCar.mileage);
            chosenCar.setCost(updatedCar.cost);

            return "Updated " + oldCarStr + " to\n " + chosenCar.toString();
        } catch (Exception exception)
        {
            return exception.getMessage();
        }
    }
    public void startUi() throws IOException {
        boolean exit = false;

        String resultMessage = "";
        while(!exit)
        {

            System.out.print(menuMessage);
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

            if (!resultMessage.isEmpty())
                System.out.println("Result:\n" + resultMessage);

            System.out.print("Enter your option:\n>>\t");
            String option = br.readLine();

            switch (option)
            {
                case "0":
                    exit = true;
                    resultMessage = "Goodbye!";
                    break;
                case "1":
                    resultMessage = viewCars();
                    break;
                case "2":
                    resultMessage = addCar();
                    break;
                case "3":
                    resultMessage = removeCar();
                    break;
                case "4":
                    resultMessage = updateCar();
                    break;
                default:
                    resultMessage = "Wrong input, try again!";
            }
        }
    }

}
