package org.project.repository;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileWriter;

import org.project.domain.DoctorAppointments;

public class DoctorAppointmentsRepositoryTextFile extends FileRepository<Integer, DoctorAppointments> {
    public DoctorAppointmentsRepositoryTextFile(String fileName) {
        super(fileName);
    }

    @Override
    protected void readFromFile()  {
        try(BufferedReader reader = new BufferedReader(new FileReader(fileName))) {
            String line = null;
            while ((line = reader.readLine())!= null) {
                String[] stringArray = line.split(",");
                if (stringArray.length != 7) {
                    continue;
                }
                    Integer id = Integer.parseInt(stringArray[0]);
                    Integer doctorId = Integer.parseInt(stringArray[1]);
                    Integer patientId = Integer.parseInt(stringArray[2]);
                    String specialization = stringArray[3];
                    String date = stringArray[4];
                    DoctorAppointments doctorAppointment = new DoctorAppointments(id, doctorId, patientId, specialization, date);
                    this.elems.put(doctorAppointment.getId(), doctorAppointment);
            }
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    protected void writeToFile() {
        try(BufferedWriter writer = new BufferedWriter(new FileWriter(fileName))) {
                for (DoctorAppointments d: this.elems.values())
                {
                    writer.write(d.getId() + "," + d.getDoctorId() + "," + d.getPatientId() + "," + d.getSpecialization() + "," + d.getAppointedTime() + '\n');
                }
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
    }
}
