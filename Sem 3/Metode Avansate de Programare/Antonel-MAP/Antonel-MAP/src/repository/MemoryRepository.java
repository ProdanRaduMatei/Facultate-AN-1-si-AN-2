package repository;

import domain.Identifiable;

import java.util.HashMap;

public class MemoryRepository<ID, Rp extends Identifiable<ID>> implements RIdentifiable<ID, Rp> {
    HashMap<ID, Rp> entities = new HashMap<>();

    @Override
    public void add(Rp object) {
        if (entities.containsKey(object.getId())) {
            return;
        }
        entities.put(object.getId(), object);
    }

    @Override
    public Rp delete(ID id) {
        if (entities.containsKey(id)) {
            return entities.remove(id);
        }
        return null;
    }

    @Override
    public Rp update(Rp object) {
        if (entities.containsKey(object.getId())) {
            entities.put(object.getId(), object);
            return null;
        }
        return object;
    }

    @Override
    public Rp findById(ID id) {
        return entities.get(id);
    }

    @Override
    public Iterable<Rp> getAll() {
        return entities.values();
    }

}
