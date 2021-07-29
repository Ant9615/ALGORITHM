public class casting { 
    // 영문으로 클래스명을 정할 떄 맨앞글자는 무조건 대문자
    public static void main(String[] args) {
        double a = 1.1;
        double b = 1; // 묵시적으로 integer
        System.out.println(b);

        // cast 
        double d = (double)1; // 명시적으로 double
        System.out.println(d);

        // 1 to string 
        String f = Integer.toString(1); // toString에서 변수로 안됨
        System.out.println(f);
    }
}
