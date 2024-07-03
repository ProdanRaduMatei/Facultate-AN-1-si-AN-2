package repository;

import domain.Doctor;

import java.io.ObjectInputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.HashMap;
import java.io.ObjectOutputStream;
import java.io.FileOutputStream;

public class DoctorRepositoryBinaryFile extends FileRepository<Integer, Doctor> {
    public DoctorRepositoryBinaryFile(String fileName) {
        super(fileName);
    }

    @Override
    protected void readFromFile() {
        try(ObjectInputStream ois = new ObjectInputStream(new FileInputStream(fileName))) {
            elems = (HashMap<Integer, Doctor>) ois.readObject();
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
