package repository;
import domain.Vehicle;

import java.io.*;
import java.util.ArrayList;
import java.util.HashMap;

public class VehicleRepositoryBinaryFile extends FileRepository<Integer, Vehicle> {
    public VehicleRepositoryBinaryFile(String fileName) {
        super(fileName);
    }

    @Override
    protected void readFromFile() {
        try {
            ObjectInputStream objectInputStream = new ObjectInputStream(new FileInputStream(fileName));
            ArrayList<Vehicle> vehicles = (ArrayList<Vehicle>) objectInputStream.readObject();
            for (Vehicle vehicle : vehicles) {
                this.add(vehicle);
            }
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }
    }

    @Override
    protected void writeToFile() {
        try {
            ObjectOutputStream objectOutputStream = new ObjectOutputStream(new FileOutputStream(fileName));
            ArrayList<Vehicle> vehicles = new ArrayList<>();
            for (Vehicle vehicle : super.getAll()) {
                vehicles.add(vehicle);
            }
            objectOutputStream.writeObject(vehicles);
            objectOutputStream.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}