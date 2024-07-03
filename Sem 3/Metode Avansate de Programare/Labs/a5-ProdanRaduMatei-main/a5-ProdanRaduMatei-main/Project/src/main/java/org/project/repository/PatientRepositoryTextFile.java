package org.project.repository;

import org.project.domain.Patient;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileWriter;

public class PatientRepositoryTextFile extends FileRepository<Integer, Patient> {
    public PatientRepositoryTextFile(String fileName) {
        super(fileName);
    }

    @Override
    protected void readFromFile() {
        try(BufferedReader reader = new BufferedReader(new FileReader(fileName))) {
            String line;
            while((line = reader.readLine()) != null) {
                String[] data = line.split(",");
                if (data.length != 6) 
                    continue;
                Patient patient = new Patient(Integer.parseInt(data[0]), data[1], data[2], data[3], data[4], data[5]);
                this.elems.put(patient.getId(), patient);
            }
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    protected void writeToFile() {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(fileName))) {
            for (Patient patient : this.elems.values()) {
                writer.write(patient.getId() + "," + patient.getName() + "," + patient.getPhone() + "," + patient.getAddress() + "," + patient.getIllness() + "," + patient.getTreatment());
                writer.newLine();
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
