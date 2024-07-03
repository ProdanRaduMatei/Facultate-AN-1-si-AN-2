package repository;

import domain.Identifiable;

public abstract class FileRepository<ID, Rp extends Identifiable<ID>> extends MemoryRepository<ID, Rp> {
    protected String fileName;
    public FileRepository(String fileName) {
        this.fileName = fileName;
        readFromFile();
    }
    protected abstract void readFromFile();
    protected abstract void writeToFile();
    @Override
    public void add(Rp elem) {
        super.add(elem);
        writeToFile();
    }
    @Override
    public Rp delete(ID id) {
        Rp elem = super.delete(id);
        writeToFile();
        return elem;
    }
    @Override
    public Iterable<Rp> getAll() {
        return super.getAll();
    }
}
