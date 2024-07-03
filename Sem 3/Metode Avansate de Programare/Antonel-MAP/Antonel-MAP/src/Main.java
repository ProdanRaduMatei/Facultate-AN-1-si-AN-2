// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
import UI.UI;
import domain.Vehicle;
import repository.VehicleRepositoryBinaryFile;
import repository.VehicleRepositoryTextFile;
import service.Service;
import repository.RIdentifiable;
import tests.UnitTesting;

public class Main {
    public static void main(String[] args) {
        UnitTesting unitTesting = new UnitTesting();
        unitTesting.runAllTests();
//        Service serv = new Service();
//        UI ui = new UI(serv);
//        ui.run();
//        RIdentifiable <Integer, Vehicle> vehRepo = new VehicleRepositoryTextFile("vehicles.txt");
//        vehRepo.add(new Vehicle(4, "Audi", "A4", "black", 2010, 10000, 100000));
//        for (Vehicle v : vehRepo.getAll()) {
//            System.out.println(v);
//        };
//        RIdentifiable<Integer, Vehicle> vehRepoBin = new VehicleRepositoryBinaryFile("vehicles.bin");
//        vehRepoBin.add(new Vehicle(1, "Audi A7", "Sedan", "Nardo Gray", 2022, 147500, 3250));
//        for (Vehicle v : vehRepoBin.getAll()) {
//            System.out.println(v);
//        }
    }
}