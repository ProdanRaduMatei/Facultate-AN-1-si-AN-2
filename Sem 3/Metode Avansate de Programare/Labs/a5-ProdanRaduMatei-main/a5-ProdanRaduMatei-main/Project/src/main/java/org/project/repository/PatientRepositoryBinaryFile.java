package org.project.repository;

import java.util.HashMap;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.FileInputStream;
import java.io.ObjectOutputStream;
import java.io.FileOutputStream;

import org.project.domain.Patient;

public class PatientRepositoryBinaryFile extends FileRepository<Integer, Patient> {
    public PatientRepositoryBinaryFile(String fileName) {
        super(fileName);
    }

    @Override
    protected void readFromFile() {
        try(ObjectInputStream ois = new ObjectInputStream(new FileInputStream(fileName))) {
            elems = (HashMap<Integer, Patient>) ois.readObject();
        } catch (IOException | ClassNotFoundException e) {
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
