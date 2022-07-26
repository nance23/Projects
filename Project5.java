import java.util.Scanner;

import static java.lang.Math.floor;

public class Project1 {
    static double saving()
    {
        double fuel_price;
        double MPG_gas;
        double KWH_Mile_EV;
        double utility_rate;
        double total_miles;

        Scanner myObj = new Scanner(System.in);  // Create a Scanner object
        System.out.println("Enter local fuel price/gallon");
        // myObj.nextLine() receives input from user
        fuel_price = Double.parseDouble((myObj.nextLine()));
        //System.out.println prints out
        System.out.println(fuel_price);
        System.out.println("Enter MpGAS price");
        MPG_gas = myObj.nextDouble();
        System.out.println(MPG_gas);
        System.out.println("Enter KWH_Mile_EV");
        KWH_Mile_EV = myObj.nextDouble();
        System.out.println(KWH_Mile_EV);
        System.out.println("utility_rate");
        utility_rate = myObj.nextDouble();
        System.out.println(utility_rate);
        System.out.println("total_miles");
        total_miles = myObj.nextDouble();
        System.out.println(total_miles);

        double results=((total_miles/ MPG_gas) * fuel_price ) - ((total_miles *  KWH_Mile_EV) *utility_rate);

        return results;
    }
    public static void main(String[] args)
    {
        // (total miles driven / MPG) x gas price per gallon ]  - [ (total miles driven x  EV kWh consumption per miles) x utility rate per kWh
        double s = floor(saving());
        System.out.println("Based on the data provided, you can save $" + s + " per year by\n" +
                "driving an EV.\n");

    }
}
