package tests;
import domain.Vehicle;
import domain.CarRental;
import domain.Customer;
import repository.FileRepository;
import repository.VehicleRepositoryBinaryFile;
import repository.VehicleRepositoryTextFile;
import service.Service;
import repository.RIdentifiable;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.Test;


public class UnitTesting {
    private Service serv = new Service();


    @Test
    public void testAddVehicle() {
        {
            Vehicle v = new Vehicle(9, "Audi A7", "Sedan", "Nardo Gray", 2022, 78200, 1500);
            serv.addVehicle(v);
            assertEquals(serv.getAllVehicles().spliterator().getExactSizeIfKnown(), 9);
        }
    }

    @Test
    public void testAddCarRental() {
        {
            CarRental c = new CarRental(4, 1, 1, 5, 17300, 1555);
            serv.addCarRental(c);
            assertEquals(serv.getAllCarRentals().spliterator().getExactSizeIfKnown(), 4);
        }
    }

    @Test
    public void testDeleteVehicle() {
        {
            serv.deleteVehicle(9);
            assertEquals(serv.getAllVehicles().spliterator().getExactSizeIfKnown(), 8);
        }
    }

    @Test
    public void testDeleteCarRental() {
        {
            serv.deleteCarRental(4);
            assertEquals(serv.getAllCarRentals().spliterator().getExactSizeIfKnown(), 3);
        }
    }

    @Test
    public void testUpdateVehicle() {
        {
            Vehicle v = new Vehicle(1, "Audi A4", "Wagon", "black", 2010, 10000, 100000);
            serv.updateVehicle(v);
            assertEquals(serv.findCarById(1).getName(), "Audi A4");
        }
    }

    @Test
    public void testUpdateCarRental() {
        {
            CarRental c = new CarRental(1, 1, 1, 5, 17300, 1555);
            serv.updateCarRental(c);
            assertEquals(serv.findRentalById(1).getDays(), 5);
        }
    }

    @Test
    public void testGetAllVehicles() {
        {
            assertEquals(serv.getAllVehicles().spliterator().getExactSizeIfKnown(), 8);
        }
    }
    Customer ctest = new Customer(5, "Florin Salam", "Laponia", "0740123456", "meow");
    @Test
    public void testCustomerName() {
        {
            assertEquals(ctest.getName(), "Florin Salam");
        }
    }
    @Test
    public void testCustomerAddress() {
        {
            assertEquals(ctest.getAddress(), "Laponia");
        }
    }
    @Test
    public void testCustomerPhoneNumber() {
        {
            assertEquals(ctest.getPhoneNumber(), "0740123456");
        }
    }
    @Test
    public void testCustomerEmail() {
        {
            assertEquals(ctest.getEmail(), "meow");
        }
    }
    @Test
    public void testCustomerID() {
        {
            assertEquals(ctest.getId(), 5);
        }
    }
    @Test
    public void testCustomerSetID() {
        {
            ctest.setId(7);
            assertEquals(ctest.getId(), 7);
        }
    }
    @Test
    public void testCustomerPrint() {
        {
            assertEquals(ctest.printCustomer(), "Customer{" +
                    "id=" + 7 +
                    ", name='" + "Florin Salam" + '\'' +
                    ", address='" + "Laponia" + '\'' +
                    ", phoneNumber='" + "0740123456" + '\'' +
                    ", email='" + "meow" + '\'' +
                    '}');
        }
    }
    Vehicle vtest = new Vehicle(10, "Volkswagen Golf", "Hatchback", "Yellow", 2016, 18750, 63256);
    @Test
    public void testVehicleName() {
        {
            assertEquals(vtest.getName(), "Volkswagen Golf");
        }
    }
    @Test
    public void testVehicleType() {
        {
            assertEquals(vtest.getType(), "Hatchback");
        }
    }
    @Test
    public void testVehicleColor() {
        {
            assertEquals(vtest.getColor(), "Yellow");
        }
    }
    @Test
    public void testVehicleYear() {
        {
            assertEquals(vtest.getYear(), 2016);
        }
    }
    @Test
    public void testVehiclePrice() {
        {
            assertEquals(vtest.getPrice(), 18750);
        }
    }
    @Test
    public void testVehicleMileage() {
        {
            assertEquals(vtest.getMileage(), 63256);
        }
    }
    @Test
    public void testVehicleID() {
        {
            assertEquals(vtest.getId(), 10);
        }
    }
    @Test
    public void testVehicleSetID() {
        {
            vtest.setId(7);
            assertEquals(vtest.getId(), 7);
        }
    }
    @Test
    public void testVehicleSetIsRented() {
        {
            vtest.setIsRented(true);
            assertTrue(vtest.getIsRented());
        }
    }
    @Test
    public void testVehicleSetName() {
        {
            vtest.setName("Audi R8");
            assertEquals(vtest.getName(), "Audi R8");
        }
    }
    @Test
    public void testVehicleSetType() {
        {
            vtest.setType("Sport Car");
            assertEquals(vtest.getType(), "Sport Car");
        }
    }
    @Test
    public void testVehicleSetColor() {
        {
            vtest.setColor("Twilight Purple");
            assertEquals(vtest.getColor(), "Twilight Purple");
        }
    }
    @Test
    public void testVehicleSetYear() {
        {
            vtest.setYear(2024);
            assertEquals(vtest.getYear(), 2024);
        }
    }
    @Test
    public void testVehicleSetPrice() {
        {
            vtest.setPrice(150000);
            assertEquals(vtest.getPrice(), 150000);
        }
    }
    @Test
    public void testVehicleSetMileage() {
        {
            vtest.setMileage(500);
            assertEquals(vtest.getMileage(), 500);
        }
    }

    @Test
    public void testVehiclePrint() {
        {
            assertEquals(vtest.printVehicle(), "Vehicle{" +
                    "id=" + 7 +
                    ", name='" + "Audi R8" + '\'' +
                    ", type='" + "Sport Car" + '\'' +
                    ", color='" + "Twilight Purple" + '\'' +
                    ", year=" + 2024 +
                    ", price=" + 150000 +
                    ", mileage=" + 500 +
                    '}');
        }
    }
    CarRental crtest = new CarRental(5, 10, 5, 12, 7540, 1449);
    @Test
    public void testCarRentalCarId() {
        {
            assertEquals(crtest.getIdVehicle(), 10);
        }
    }
    @Test
    public void testCarRentalCustomerId() {
        {
            assertEquals(crtest.getIdCustomer(), 5);
        }
    }
    @Test
    public void testCarRentalDays() {
        {
            assertEquals(crtest.getDays(), 12);
        }
    }
    @Test
    public void testCarRentalKilometers() {
        {
            assertEquals(crtest.getKilometers(), 7540);
        }
    }
    @Test
    public void testCarRentalPrice() {
        {
            assertEquals(crtest.getPrice(), 1449);
        }
    }
    @Test
    public void testCarRentalSetID() {
        {
            crtest.setId(7);
            assertEquals(crtest.getId(), 7);
        }
    }
    @Test
    public void testCarRentalPrint() {
        {
            assertEquals(crtest.printCarRental(), "CarRental{" +
                    "id=" + 7 +
                    ", idVehicle=" + 10 +
                    ", idCustomer=" + 5 +
                    ", days=" + 12 +
                    ", kilometers=" + 7540 +
                    ", price=" + 1449 +
                    '}');
        }
    }


    @Test
    public void testTextFileRepository() {
        RIdentifiable <Integer, Vehicle> vehRepo = new VehicleRepositoryTextFile("vehicles.txt");
        Vehicle v = new Vehicle(5, "Audi A7", "Sedan", "Nardo Gray", 2022, 78200, 1500);
        vehRepo.add(v);
        assertEquals(vehRepo.getAll().spliterator().getExactSizeIfKnown(), 5);
        vehRepo.delete(5);
        assertEquals(vehRepo.getAll().spliterator().getExactSizeIfKnown(), 4);
        Vehicle v2 = new Vehicle(1, "Audi A4", "Wagon", "black", 2010, 10000, 100000);
        vehRepo.update(v2);
        assertEquals(vehRepo.findById(1).getName(), "Audi A4");
        assertEquals(vehRepo.findById(1).getType(), "Wagon");
        assertEquals(vehRepo.findById(1).getColor(), "black");
        assertEquals(vehRepo.findById(1).getYear(), 2010);
        assertEquals(vehRepo.findById(1).getPrice(), 10000);
        assertEquals(vehRepo.findById(1).getMileage(), 100000);
        assertEquals(vehRepo.findById(1).getId(), 1);
        Vehicle v3 = new Vehicle(6, "Audi A7", "Sedan", "Nardo Gray", 2022, 78200, 1500);
        vehRepo.add(v3);
        assertEquals(vehRepo.getAll().spliterator().getExactSizeIfKnown(), 5);
        vehRepo.delete(6);
        assertEquals(vehRepo.getAll().spliterator().getExactSizeIfKnown(), 4);
    }

    @Test
    public void testBinaryFileRepository() {
        RIdentifiable <Integer, Vehicle> vehRepo = new VehicleRepositoryBinaryFile("vehicles.bin");
        Vehicle v = new Vehicle(1, "Audi A7", "Sedan", "Nardo Gray", 2022, 78200, 1500);
        vehRepo.add(v);
        assertEquals(vehRepo.getAll().spliterator().getExactSizeIfKnown(), 1);
        vehRepo.delete(1);
        assertEquals(vehRepo.getAll().spliterator().getExactSizeIfKnown(), 0);
        Vehicle v2 = new Vehicle(1, "Audi A4", "Wagon", "black", 2010, 10000, 100000);
        vehRepo.add(v);
        vehRepo.update(v2);
        assertEquals(vehRepo.findById(1).getName(), "Audi A4");
        assertEquals(vehRepo.findById(1).getType(), "Wagon");
        assertEquals(vehRepo.findById(1).getColor(), "black");
        assertEquals(vehRepo.findById(1).getYear(), 2010);
        assertEquals(vehRepo.findById(1).getPrice(), 10000);
        assertEquals(vehRepo.findById(1).getMileage(), 100000);
        assertEquals(vehRepo.findById(1).getId(), 1);
        Vehicle v3 = new Vehicle(2, "Audi A7", "Sedan", "Nardo Gray", 2022, 78200, 1500);
        vehRepo.add(v3);
        assertEquals(vehRepo.getAll().spliterator().getExactSizeIfKnown(), 2);
        vehRepo.delete(2);
        assertEquals(vehRepo.getAll().spliterator().getExactSizeIfKnown(), 1);
    }


    public void runAllTests() {
        testAddVehicle();
        testAddCarRental();
        testDeleteVehicle();
        testDeleteCarRental();
        testUpdateVehicle();
        testUpdateCarRental();
        testGetAllVehicles();
        testCustomerName();
        testCustomerAddress();
        testCustomerPhoneNumber();
        testCustomerEmail();
        testCustomerID();
        testCustomerSetID();
        testCustomerPrint();
        testVehicleName();
        testVehicleType();
        testVehicleColor();
        testVehicleYear();
        testVehiclePrice();
        testVehicleMileage();
        testVehicleID();
        testVehicleSetID();
        testVehicleSetIsRented();
        testVehicleSetName();
        testVehicleSetType();
        testVehicleSetColor();
        testVehicleSetYear();
        testVehicleSetPrice();
        testVehicleSetMileage();
        testVehiclePrint();
        testCarRentalCarId();
        testCarRentalCustomerId();
        testCarRentalDays();
        testCarRentalKilometers();
        testCarRentalPrice();
        testCarRentalSetID();
        testCarRentalPrint();
        testTextFileRepository();
        testBinaryFileRepository();
    }

}
