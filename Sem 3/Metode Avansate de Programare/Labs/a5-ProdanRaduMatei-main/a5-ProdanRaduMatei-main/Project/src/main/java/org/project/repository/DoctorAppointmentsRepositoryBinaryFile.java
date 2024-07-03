package org.project.repository;

import java.io.ObjectInputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.HashMap;
import java.io.ObjectOutputStream;
import java.io.FileOutputStream;

import org.project.domain.DoctorAppointments;

public class DoctorAppointmentsRepositoryBinaryFile extends FileRepository<Integer, DoctorAppointments> {
    public DoctorAppointmentsRepositoryBinaryFile(String fileName) {
        super(fileName);
    }

    @Override
    protected void readFromFile() {
        try(ObjectInputStream ois = new ObjectInputStream(new FileInputStream(fileName))) {
            elems = (HashMap<Integer, DoctorAppointments>) ois.readObject();
        } catch (IOException e) {
            throw new RuntimeException(e);
        } catch (ClassNotFoundException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    protected void writeToFile() {
        try(ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(fileName))) {
            oos.writeObject(elems);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
