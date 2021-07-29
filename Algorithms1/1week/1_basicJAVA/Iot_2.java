import org.opentutorials.iot.Elevator;
import org.opentutorials.iot.Security;
import org.opentutorials.iot.Lighting;

public class Iot_2 {
    public static void main(String[] args) {
        String APT_id = "JAVA APT 507";

        // ELEVATOR
        Elevator myElevator = new Elevator(APT_id); 
        myElevator.callForUp(2);

        //Security 
        Security mySecurity = new Security(APT_id);
        mySecurity. on();

        // LIGHT
        Lighting halllamp = new Lighting(APT_id+"/hall lamp");
        halllamp.off();

        Lighting floorlamp = new Lighting(APT_id+"/floor lamp");
        floorlamp.off();

    }
}
