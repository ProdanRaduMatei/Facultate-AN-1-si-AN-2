package service;
import domain.Vehicle;
import domain.CarRental;
import domain.Customer;
import repository.VehicleRepository;
import repository.RentalsRepository;

public class Service {
    private VehicleRepository vehicleRepository = new VehicleRepository();
    private RentalsRepository rentalsRepository = new RentalsRepository();
    private void initService() {
        vehicleRepository.add(new Vehicle(1, "Ford Focus", "Sedan", "Red", 2015, 5400, 148700));
        vehicleRepository.add(new Vehicle(2, "Dacia Logan", "Sedan", "White", 2017, 9800, 30570));
        vehicleRepository.add(new Vehicle(3, "BMW X5", "SUV", "Black", 2019, 100000, 104000));
        vehicleRepository.add(new Vehicle(4, "Audi A4", "Sedan", "Silver", 2018, 31900, 67540));
        vehicleRepository.add(new Vehicle(5, "Volkswagen Golf", "Hatchback", "Yellow", 2016, 18750, 63256));
        vehicleRepository.add(new Vehicle(6, "Mercedes-Benz AMG E63S", "Sedan", "Black", 2019, 240000, 7500));
        vehicleRepository.add(new Vehicle(7, "Audi RSQ7", "SUV", "Carbon Red", 2017, 90000, 90000));
        vehicleRepository.add(new Vehicle(8, "BMW M340i", "Sedan", "Laguna Blue", 2018, 70000, 14500));
        Customer customer = new Customer(1, "Antonel Smecherescu", "Aleea Valeriu Bologa 3", "0740123456", "antonioadelin@gmail.com");
        Customer customer2 = new Customer(2, "Pista Matei Bomba", "Aleea Smecherilor 43", "0740123456", "pista_smek@yahoo.com");
        Customer customer3 = new Customer(3, "Mihai Pocinan", "Calea Victoriei 69", "0740123456", "mihai25@gmail.com");
        rentalsRepository.add(new CarRental(1, 1, 1, 5, 17300, 1555));
        rentalsRepository.add(new CarRental(2, 2, 2, 3, 24000, 1440));
        rentalsRepository.add(new CarRental(3, 6, 3, 7, 2500, 57320));

    };

    public Service() {
        initService();
    }
    
    public void addCarRental(CarRental carRental) {
        rentalsRepository.add(carRental);
    }

    public void deleteVehicle(Integer id) {
        vehicleRepository.delete(id);
    }

    public void addVehicle(Vehicle vehicle) {
        vehicleRepository.add(vehicle);
    }

    public Vehicle findCarById(Integer id) {
        return vehicleRepository.findById(id);
    }

    public CarRental findRentalById(Integer id) {
        return rentalsRepository.findById(id);
    }


    public void deleteCarRental(Integer id) {
        rentalsRepository.delete(id);
    }

    public void updateVehicle(Vehicle vehicle) {
        vehicleRepository.update(vehicle);
    }

    public void updateCarRental(CarRental carRental) {
        rentalsRepository.update(carRental);
    }

    public Iterable<Vehicle> getAllVehicles() {
        return vehicleRepository.getAll();
    }

    public Iterable<CarRental> getAllCarRentals() {
        return rentalsRepository.getAll();
    }}
