package repository;

import domain.Identifiable;

import java.util.HashMap;
import java.util.Map;

public class MemoryRepository<ID, T extends Identifiable<ID>> implements IRepository<ID, T> {
    HashMap<ID, T> data = new HashMap<ID, T>();
    @Override
    public T add(T element) {

        return data.put(element.getId(), element);
    }

    @Override
    public T delete(ID id) {
        return data.remove(id);
    }

    @Override
    public T update(ID id, T newElement) {
        return data.replace(id, newElement);
    }

    @Override
    public T findById(ID id) {
        return data.get(id);
    }

    @Override
    public Iterable<T> getAll() {

        return data.values();
    }

    @Override
    public int size()
    {
        return data.size();
    }
}
