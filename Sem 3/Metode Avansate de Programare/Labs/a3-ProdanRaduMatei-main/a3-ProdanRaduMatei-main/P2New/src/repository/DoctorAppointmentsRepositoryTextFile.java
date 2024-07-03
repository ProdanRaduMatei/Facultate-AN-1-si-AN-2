package repository;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileWriter;

import domain.DoctorAppointments;

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
                    String name = stringArray[1];
                    String specialization = stringArray[2];
                    String address = stringArray[3];
                    String phone = stringArray[4];
                    Boolean isAppointed = Boolean.parseBoolean(stringArray[5]);
                    String date = stringArray[6];
                    DoctorAppointments doctorAppointment = new DoctorAppointments(id, name, specialization, address, phone, isAppointed, date);
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
                    writer.write(d.getId() + "," + d.getName() + "," + d.getPhone() + "," + d.getAddress() + "," + d.getSpecialization() + "," + d.getIsAppointed() + "," + d.getAppointedTime() + '\n');
                }
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
    }
}
