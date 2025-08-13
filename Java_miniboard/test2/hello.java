    // hello : 클래스 블록. public은 접근 제어자로 어디서든 이 클래스에 접근가능.
            // class는 클래스 블록을 만드는 키워드.
            // 클래스명은 명사 / 대문자로시작/ 단어조합시 파스칼케이스(ex:ChocoCookie)로 사용 
public class hello {
    // main : 메서드. 클래스 블록안엔 여러가지 메서드가 존재할 수 있다.
            // 메서드명은 동사 / 소문자로시작/ 단어조합시 카멜케이스로 사용.
    // static : 메서드에 static이 붙으면 클래스 메서드가 되어 객체를 만들지 않아도 '클래스명.메서드명'
    //          형태로 호출할 수 있다.
    // void : 리턴값이 없음을 뜻함.
    // String[] args : 메서드의 매개 변수. args 변수는 string형태의 배열자료임을 뜻함. args는 변수로
    //                  다른 이름으로 사용할수 있다.
    public static void main(String[] args) {
        // statement(명령문) : 컴퓨터에 무언가 일을 시키는 문장. 
        System.out.println("Hello java");

        // 변수(variable)
        // 1. 변수명은 숫자로 시작할 수 없다.
        // 2. _와 $외의 특수 문자는 사용할 수 없다.
        // 3. int, class, return 등 자바키워드는 변수명으로 사용할 수 없다.
        int one;
        // int one : 변수 one의 자료형은 int다. 1,10,24 같은 정수만 담을 수 있다.
        String two;
        // String two : 변수 two의 자료형은 string으로 "a","hello"등의 문자열만 담을 수 있다.
    }

}
/* 클래스나 메서드등을 설명할 때 주로 사용함 */
/* 지금만든 hello클래스는 틀렸다..Hello가 되어야한다. */
