package hello; 

// 패키지명 = 해당 폴더명
// 클래스명 = 해당 파일명
public class HelloWorld {
    public static void main(String args[]){
        System.out.println("Hello World");
    }
}

// public: 메소드 접근제어자(정처기 떠올리셈)
// static: 해당 메소드는 인스턴스 생성없이 실행가능 
// void: 메소드의 리턴값 없음 
// system.out.println: 표준출력으로 데이터를 보내는 자바의 내장 메소드 
//                      문자열을 화면에 출력