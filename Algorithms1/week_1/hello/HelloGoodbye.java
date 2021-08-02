package hello;
import java.util.Scanner;
import java.util.Arrays;


public class HelloGoodbye {
    public static void main(String[] args){
        String name;
        String[] names;

        Scanner sc = new Scanner(System.in);
        System.out.println("java HelloGoodbye "); 
        name = sc.next();
        names = name.split(" ");
        System.out.printf("Hello %s and %s", names[0], names[1]);
    }
}
