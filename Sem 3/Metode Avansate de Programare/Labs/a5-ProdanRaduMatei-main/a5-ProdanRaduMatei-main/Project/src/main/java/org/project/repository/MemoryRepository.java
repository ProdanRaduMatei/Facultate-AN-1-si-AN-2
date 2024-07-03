package org.project.repository;

import org.project.domain.Identifiable;

import java.util.HashMap;

public class MemoryRepository<ID, T extends Identifiable<ID>> implements IRepository<ID, T> {
    protected HashMap<ID, T> elems = new HashMap<ID, T>();

    public void add(T elem) {
        if (elems.containsKey(elem.getId()))
            throw new RuntimeException("Element with id " + elem.getId() + " already exists!");
        else
            elems.put(elem.getId(), elem);
    }

    public void delete(ID id) {
        if (elems.containsKey(id))
            elems.remove(id);
        else
            throw new RuntimeException("Element with id " + id + " does not exist!");
    }

    public void update(ID id, T newElem) {
        if (elems.containsKey(id))
            elems.put(id, newElem);
        else
            throw new RuntimeException("Element with id " + id + " does not exist!");
    }

    public T findByID(ID id) {
        if (elems.containsKey(id))
            return elems.get(id);
        else
            throw new RuntimeException("Element with id " + id + " does not exist!");
    }

    public Iterable<T> getAll() {
        return elems.values();
    }
}
