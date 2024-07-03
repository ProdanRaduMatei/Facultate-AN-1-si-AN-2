import ui.Ui;


public class App {



    public static void main(String[] args) {
        try {
            Ui ui = new Ui();
            ui.startUi();
        }
        catch (Exception e)
        {
            System.out.println("I don't know what you did, but good job!");
            System.out.println(e.getMessage());
        }
    }
}

