package domain;

public class CarRental implements Identifiable<Integer> {
    private Integer id;
    private Integer idVehicle;
    private Integer idCustomer;
    private Integer days;
    private Integer kilometers;
    private Integer price;

    public CarRental(Integer id, Integer idVehicle, Integer idCustomer, Integer days, Integer kilometers, Integer price) {
        this.id = id;
        this.idVehicle = idVehicle;
        this.idCustomer = idCustomer;
        this.days = days;
        this.kilometers = kilometers;
        this.price = price;
    }

    @Override
    public Integer getId() {
        return id;
    }

    @Override
    public void setId(Integer id){
        this.id = id;
    }

    public Integer getIdVehicle() {
        return idVehicle;
    }

    public Integer getIdCustomer() {
        return idCustomer;
    }

    public Integer getDays() {
        return days;
    }

    public Integer getKilometers() {
        return kilometers;
    }

    public Integer getPrice() {
        return price;
    }

    public String printCarRental(){
        return "CarRental{" +
                "id=" + id +
                ", idVehicle=" + idVehicle +
                ", idCustomer=" + idCustomer +
                ", days=" + days +
                ", kilometers=" + kilometers +
                ", price=" + price +
                '}';
    }
}
