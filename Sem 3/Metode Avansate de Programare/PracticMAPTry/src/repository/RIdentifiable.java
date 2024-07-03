package repository;

import domain.Identifiable;

public interface RIdentifiable<ID, Rp extends Identifiable<ID>> {
    void add(Rp object);

    Rp delete(ID id);

    Rp update(Rp object);

    Rp findById(ID id);

    Iterable<Rp> getAll();
}
