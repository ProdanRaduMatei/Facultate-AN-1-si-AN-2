package UI;
import domain.Vehicle;
import domain.CarRental;
import domain.Customer;
import service.Service;

import java.util.Scanner;

public class UI {
    private Service serv = new Service();
    public UI(Service serv) {
        this.serv = serv;
    }

    public static void printMenu() {
        System.out.println("1. Add a car");
        System.out.println("2. Add a rental");
        System.out.println("3. Delete a car");
        System.out.println("4. Delete a rental");
        System.out.println("5. Update a car");
        System.out.println("6. Update a rental");
        System.out.println("7. Print all cars");
        System.out.println("8. Print all rentals");
        System.out.println("9. Print all");
        System.out.println("10. Exit");
    }

    public void run() {
        while (true) {
            printMenu();
            Scanner scanner = new Scanner(System.in);
            int option = scanner.nextInt();
            if (option == 0) {
                break;
            }
            switch (option) {
                case 1:
                    this.addCar();
                    break;
                case 2:
                    this.addRental();
                    break;
                case 3:
                    this.deleteCar();
                    break;
                case 4:
                    this.deleteRental();
                    break;
                case 5:
                    this.updateCar();
                    break;
                case 6:
                    this.updateRental();
                    break;
                case 7:
                    this.printAllCars();
                    break;
                case 8:
                    this.printAllRentals();
                    break;
                case 9:
                    this.printAll();
                    break;
                case 10:
                    System.out.println("Thank you for using our app!");
                    return;
                default:
                    System.out.println("Invalid option!");
                    break;
            }
        }
    }

    private void printAll() {
        for (Vehicle vehicle : serv.getAllVehicles()) {
            System.out.println(vehicle.printVehicle());
        }
        for (CarRental carRental : serv.getAllCarRentals()) {
            System.out.println(carRental.printCarRental());
        }
    }

    private void printAllRentals() {
        for (CarRental carRental : serv.getAllCarRentals()) {
            System.out.println(carRental.printCarRental());
        }
    }

    private void printAllCars() {
        for (Vehicle vehicle : serv.getAllVehicles()) {
            System.out.println(vehicle.printVehicle());
        }
    }

    private void updateRental() {
        CarRental carRental = inputRental();
        try {
            serv.updateCarRental(carRental);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    private CarRental inputRental() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the id: ");
        Integer id = scanner.nextInt();
        System.out.println("Enter the car id: ");
        Integer carId = scanner.nextInt();
        System.out.println("Enter the customer id: ");
        Integer customerId = scanner.nextInt();
        System.out.println("Enter the number of days: ");
        Integer days = scanner.nextInt();
        System.out.println("Enter the mileage: ");
        Integer mileage = scanner.nextInt();
        System.out.println("Enter the price: ");
        Integer price = scanner.nextInt();
        return new CarRental(id, carId, customerId, days, mileage, price);
    }

    private Customer inputCustomer() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the id: ");
        Integer id = scanner.nextInt();
        System.out.println("Enter the name: ");
        String name = scanner.next();
        System.out.println("Enter the address: ");
        String address = scanner.next();
        System.out.println("Enter the phone number: ");
        String phoneNumber = scanner.next();
        System.out.println("Enter the email: ");
        String email = scanner.next();
        return new Customer(id, name, address, phoneNumber, email);
    }

    private void updateCar() {
        Vehicle vehicle = inputCar();
        try {
            serv.updateVehicle(vehicle);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    private Vehicle inputCar() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the id: ");
        Integer id = scanner.nextInt();
        System.out.println("Enter the name: ");
        String name = scanner.next();
        System.out.println("Enter the type: ");
        String type = scanner.next();
        System.out.println("Enter the color: ");
        String color = scanner.next();
        System.out.println("Enter the year: ");
        Integer year = scanner.nextInt();
        System.out.println("Enter the price: ");
        Integer price = scanner.nextInt();
        System.out.println("Enter the mileage: ");
        Integer mileage = scanner.nextInt();
        return new Vehicle(id, name, type, color, year, price, mileage);
    }

    private void deleteRental() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the id: ");
        Integer id = scanner.nextInt();
        try {
            serv.deleteCarRental(id);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    private void deleteCar() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the id: ");
        Integer id = scanner.nextInt();
        try {
            serv.deleteVehicle(id);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    private void addRental() {
        CarRental rental = inputRental();
        try {
            serv.addCarRental(rental);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    private void addCar() {
        Vehicle vehicle = inputCar();
        try {
            serv.addVehicle(vehicle);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }


}
