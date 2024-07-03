package org.project.repository;

import org.project.domain.Doctor;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileWriter;

public class DoctorRepositoryTextFile extends FileRepository<Integer, Doctor> {
    public DoctorRepositoryTextFile(String fileName) {
        super(fileName);
    }

    @Override
    protected void readFromFile() {
        try(BufferedReader br = new BufferedReader(new FileReader(fileName))) {
            String line = null;
            while((line = br.readLine()) != null) {
                String[] stringArray = line.split(",");
                if(stringArray.length != 5) {
                    continue;
                }
                Integer id = Integer.parseInt(stringArray[0]);
                String name = stringArray[1];
                String phone = stringArray[2];
                String address = stringArray[3];
                String specialization = stringArray[4];
                Doctor doctor = new Doctor(id, name, phone, address, specialization);
                this.elems.put(doctor.getId(), doctor);
            }
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    protected void writeToFile() {
        try (BufferedWriter bw = new BufferedWriter(new FileWriter(fileName))) {
            for (Doctor doctor : this.elems.values()) {
                bw.write(doctor.getId() + "," + doctor.getName() + "," + doctor.getPhone() + "," + doctor.getAddress() + "," + doctor.getSpecialization());
                bw.newLine();
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
