package repository;

import domain.Vehicle;

import java.io.*;

public class VehicleRepositoryTextFile extends FileRepository<Integer, Vehicle> {
    public VehicleRepositoryTextFile(String fileName) {
        super(fileName);
    }

    @Override
    protected void readFromFile() {
        try {
            BufferedReader bufferedReader = new BufferedReader(new FileReader(fileName));
            String line = null;
            while ((line = bufferedReader.readLine()) != null) {
                String[] stringArray = line.split(";");
                if (stringArray.length != 7) {
                    System.out.println("Invalid line: " + line);
                    continue;
                } else {
                    Vehicle vehicle = new Vehicle(Integer.parseInt(stringArray[0].trim()), stringArray[1].trim(), stringArray[2].trim(), stringArray[3].trim(), Integer.parseInt(stringArray[4].trim()), Integer.parseInt(stringArray[5].trim()), Integer.parseInt(stringArray[6].trim()));
                    this.add(vehicle);
                }

            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Override
    protected void writeToFile() {
        try {
            BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(fileName));
            for (Vehicle vehicle : super.getAll()) {
                bufferedWriter.write(vehicle.getId() + ";" + vehicle.getName() + ";" + vehicle.getType() + ";" + vehicle.getColor() + ";" + vehicle.getYear() + ";" + vehicle.getPrice() + ";" + vehicle.getMileage() + "\n");
            }
            bufferedWriter.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
