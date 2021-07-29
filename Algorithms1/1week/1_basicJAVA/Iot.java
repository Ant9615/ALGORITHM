import javax.swing.JOptionPane;

import org.opentutorials.iot.DimmingLights;
import org.opentutorials.iot.Elevator;
import org.opentutorials.iot.Lighting;
import org.opentutorials.iot.Security;

public class Iot {
    public static void main(String[] args) {
        String id = JOptionPane.showInputDialog("Enter a ID"); // input
        String bright = JOptionPane.showInputDialog("Enter a Bright level"); // input
        
        
        // elevator call 
        Elevator myElevator = new Elevator(id); 
        //class import 할때 디렉토리 잘 보고 해당 패키지 불러올 때 class 명(elevator) 선책하고 "ctrl+."하면 import 명령문 자동생성됨
        // https://hianna.tistory.com/585
        myElevator.callForUp(1);
        
        // security off 
        Security mySecurity = new Security(id);
        mySecurity.off();

        //light on
        Lighting hallamp = new Lighting(id+"/ Hall Lamp");
        hallamp.on();
        
        Lighting floorLamp = new Lighting(id+"/ floorLamp");
        floorLamp.on();

        DimmingLights moodLamp = new DimmingLights(id+"moodLamp");
        moodLamp.setBright(Double.parseDouble(bright));
        moodLamp.on();
    }
}

// 디버거는 디버깅을 수행할 때 사용하는 도구임
// 디버거를 사용하면 한줄씩 사용가능, 변수상태 확인가능함
// 