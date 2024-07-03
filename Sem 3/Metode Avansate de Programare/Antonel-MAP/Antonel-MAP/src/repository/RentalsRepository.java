package repository;

import domain.CarRental;

public class RentalsRepository extends MemoryRepository<Integer, CarRental> {
    public RentalsRepository() {
        super();
    }

    @Override
    public CarRental update(CarRental object) {
        if (entities.containsKey(object.getId())) {
            entities.put(object.getId(), object);
            return null;
        }
        return object;
    }

}
