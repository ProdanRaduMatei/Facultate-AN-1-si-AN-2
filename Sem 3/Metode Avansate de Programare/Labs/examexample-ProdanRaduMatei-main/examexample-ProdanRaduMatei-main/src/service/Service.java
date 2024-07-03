package service;

import repository.Repository;
import domain.Bus;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class Service {
    private Repository repo;

    public Service(Repository repo) {
        repo = new Repository("buses");
        this.repo = repo;
    }

    public void initRepo() {
        if (this.repo != null) {
            repo.add(new Bus(1, "Cluj-Napoca", "Bucuresti", 12, 20, 20, 5, 100));
            repo.add(new Bus(2, "Cluj-Napoca", "Constanta", 10, 22, 20, 5, 150));
            repo.add(new Bus(3, "Bucuresti", "Cluj-Napoca", 10, 18, 20, 0, 100));
            repo.add(new Bus(4, "Bucuresti", "Timisoara", 8, 20, 20, 10, 150));
        }
        else
            System.out.println("Repository is not initialized!");
    }

    public void addBus(Integer id, String sourceCity, String destinationCity, Integer departureTime, Integer arrivalTime, Integer totalSeats, Integer leftSeats, Integer ticketPrice) {
        Bus newBus = new Bus(id, sourceCity, destinationCity, departureTime, arrivalTime, totalSeats, leftSeats, ticketPrice);
        repo.add(newBus);
    }

    public void removeBus(Integer id) {
        repo.delete(id);
    }

    public void updateBus(Integer id, String sourceCity, String destinationCity, Integer departureTime, Integer arrivalTime, Integer totalSeats, Integer leftSeats, Integer ticketPrice) {
        Bus newBus = new Bus(id, sourceCity, destinationCity, departureTime, arrivalTime, totalSeats, leftSeats, ticketPrice);
        repo.update(id, newBus);
    }

    public Bus getBusById(Integer id) {
        return repo.findByID(id);
    }

    public ArrayList<Bus> getAllBusses() {
        ArrayList<Bus> busesList = new ArrayList<>();
        Iterable<Bus> buses = repo.getAll();
        for (Bus bus : buses) {
            busesList.add(bus);
        }
        return busesList;
    }

    public List<Bus> getBusesByCityAndTime(String city, Integer departureTime) {
        List<Bus> busesList = new ArrayList<>();
        busesList = getAllBusses();
        List<Bus> sortedBuses = busesList.stream().filter(bus -> bus.getSourceCity().equals(city) && bus.getDepartureTime() >= departureTime).collect(Collectors.toList());
        return sortedBuses;
    }
}
