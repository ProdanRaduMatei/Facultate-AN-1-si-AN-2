package domain;

import java.util.Objects;

public class Bus {
    //A route has a source city, a destination city, the departure and arrival times, the total
    //available number of seats and the price for one ticket.
    private String sourceCity, destinationCity;
    private int id, totalSeats, leftSeats, ticketPrice, departureTime, arrivalTime;

    public Bus() {
        this.id = 0;
        this.sourceCity = "";
        this.destinationCity = "";
        this.departureTime = 0;
        this.arrivalTime = 0;
        this.totalSeats = 0;
        this.leftSeats = 0;
        this.ticketPrice = 0;
    }

    public Bus(int id, String sourceCity, String destinationCity, int departureTime, int arrivalTime, int totalSeats, int leftSeats, int ticketPrice) {
        this.id = id;
        this.sourceCity = sourceCity;
        this.destinationCity = destinationCity;
        this.departureTime = departureTime;
        this.arrivalTime = arrivalTime;
        this.totalSeats = totalSeats;
        this.leftSeats = totalSeats;
        this.ticketPrice = ticketPrice;
    }



    public int getId() {
        return id;
    }
    public String getSourceCity() {
        return sourceCity;
    }
    public String getDestinationCity() {
        return destinationCity;
    }
    public int getDepartureTime() {
        return departureTime;
    }
    public int getArrivalTime() {
        return arrivalTime;
    }
    public int getTotalSeats() {
        return totalSeats;
    }
    public int getLeftSeats() {
        return leftSeats;
    }
    public int getTicketPrice() {
        return ticketPrice;
    }

    public void setId(int id) {
        this.id = id;
    }
    public void setSourceCity(String sourceCity) {
        this.sourceCity = sourceCity;
    }
    public void setDestinationCity(String destinationCity) {
        this.destinationCity = destinationCity;
    }
    public void setDepartureTime(int departureTime) {
        this.departureTime = departureTime;
    }
    public void setArrivalTime(int arrivalTime) {
        this.arrivalTime = arrivalTime;
    }
    public void setTotalSeats(int totalSeats) {
        this.totalSeats = totalSeats;
    }
    public void setLeftSeats(int leftSeats) {
        this.leftSeats = leftSeats;
    }
    public void setTicketPrice(int ticketPrice) {
        this.ticketPrice = ticketPrice;
    }

    @Override
    public String toString() {
        return "Bus: " +
                "id = " + id + '\'' +
                ", source city = " + sourceCity + '\'' +
                ", destination city = " + destinationCity + '\'' +
                ", departure time = " + departureTime + '\'' +
                ", arrival time = " + arrivalTime + '\'' +
                ", total number of seats = " + totalSeats +
                ", remaining number of seats = " + leftSeats +
                ", ticket price = " + ticketPrice +
                ".\n";
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null || getClass() != obj.getClass())
            return false;
        Bus bus = (Bus) obj;
        return Objects.equals(id, bus.id);
    }
}
