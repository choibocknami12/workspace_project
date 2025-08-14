import java.util.Arrays;

public class ExampleString {
    public static void main(String[] args) {
        // 문자열 표시
        String a = "Happy Java";
        String b = new String("123");
        // 변수 a,b 모두 문자열을 표시하는 방식
        // 차이점 : 변수a는 리터럴(literal)표기법. 이는 자료형의 값을 직접 표현하는 방식이다.
        // String은 리터럴 표기방식을 사용할 수 있지만 원시 자료형에 포함되지 않는다.

        /* 원시자료형에는 이에 대응하는 wrapper클래스가 있다.
            wrapper 클래스는 멀티스레드 환경에서 동기화를 지원할 때 사용해야한다.
            ex : int -> Integer, boolean -> Boolean 등 */
        
        String c = "hello";
        String d = new String("hello");
        System.out.println(c.equals(d));  // true
        System.out.println(c == d);  // false
        // 문자열의 값을 비교할때는 반드시 equals을 사용해야한다.
        // ==은 자료형이 같은 객체인지를 판별할 때 사용하는 연산자라,
        // c와 d는 값은 같지만 서로 다른 객체라 false를 리턴한다. 

        String e = "Hello Java";
        System.out.println(e.indexOf("Java")); // 6출력.
        // indexOf : 문자열에서 특정 문자열이 시작되는 위치(인덱스값)를 리턴.
        // 6이 출력되는 이유는 0부터 숫자셈.

        String f = "Hello Java";
        System.out.println(f.contains("Java")); // true출력
        // contains : 특정문자열이 포함되어 있는지 여부를 리턴.

        String g = "Hello Java";
        System.out.println(g.charAt(6));  // "J" 출력
        // charAt : 문자열에서 특정 위치의 문자를 리턴.

        String h = "Hello Java";
        System.out.println(h.replaceAll("Java", "World"));  // Hello World 출력
        // replaceAll : 문자열에서 특정 문자열을 다른 문자열로 바꿀 때 사용.

        String i = "Hello Java";
        System.out.println(i.substring(0, 4));  // Hell 출력
        // substring : 문자열에서 특정 문자열을 뽑아낼 때 사용. 시작위치 <= a < 끝위치 (마지막자리는 포함안댐.)

        String j = "Hello Java";
        System.out.println(j.toUpperCase());  // HELLO JAVA 출력
        // toUpperCase : 문자열을 모두 대문자로 변경할 때 사용. 소문자는 반대로 toLowerCase 사용.

        String k = "a:b:c:d";
        String[] result = k.split(":");  // result는 {"a", "b", "c", "d"}
        System.out.println(Arrays.toString(result));
        // split : 문자열을 특정한 구분자로 나누어 문자열 배열로 리턴한다.
        // 뭔소린지 모르겠음.
    }
}
