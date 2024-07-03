package repository;

import domain.Vehicle;

public class VehicleRepository extends MemoryRepository<Integer, Vehicle> {
    public VehicleRepository() {
        super();
    }

    @Override
    public Vehicle update(Vehicle object) {
        if (entities.containsKey(object.getId())) {
            entities.put(object.getId(), object);
            return null;
        }
        return object;
    }
}
