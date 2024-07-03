package repository;

import domain.Identifiable;

public interface IRepository<ID, T extends Identifiable<ID>> {
    public void add(T elem);

    public void delete(ID id);

    public void update(ID id, T newElem);

    public T findByID(ID id);

    public Iterable<T> getAll();
}
