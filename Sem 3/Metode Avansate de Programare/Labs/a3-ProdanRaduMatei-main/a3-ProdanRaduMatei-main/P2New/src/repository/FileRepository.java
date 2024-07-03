package repository;

import domain.Identifiable;

public abstract class FileRepository<ID, T extends Identifiable<ID>> extends MemoryRepository<ID, T> {
    protected String fileName;

    public FileRepository(String fileName) {
        this.fileName = fileName;
        this.readFromFile();
    }

    protected abstract void readFromFile();
    protected abstract void writeToFile();

    @Override
    public void add(T elem) {
        super.add(elem);
        this.writeToFile();
    }

    @Override
    public void delete(ID id) {
        super.delete(id);
        this.writeToFile();
    }

    @Override
    public void update(ID id, T elem) {
        super.update(id, elem);
        this.writeToFile();
    }

    @Override
    public T findByID(ID id) {
        return super.findByID(id);
    }

    @Override
    public Iterable<T> getAll() {
        return super.getAll();
    }
}
