public class ExampleStringBuffer {
    // StringBuffer : 문자열을 추가하거나 변경할 때 주로 사용하는 자료형이다.
    public static void main(String[] args) {
        // 1. append : 문자열 추가 메서드.
        StringBuffer sb = new StringBuffer();  // StringBuffer 객체 sb 생성
        sb.append("hello");
        sb.append(" ");
        sb.append("jump to java");
        String resultA = sb.toString();
        System.out.println(resultA);  // "hello jump to java" 출력

        String resultB = ""; // 빈 문자열
        resultB += "hello"; // "" + "hello"
        resultB += " "; // "hello" + ""
        resultB += "jump to java"; // "hello" + "jump to java" 
        System.out.println(resultB);  // "hello jump to java" 출력
        // String 자료형은 값이 한번 생성되면 변경 할 수가 없다. toUpperCase와 같은 메서드를 보면 문자열이 변경되는 것처럼 보이지만,
        // 해당 메서드를 수행할 때 또 다른 String 객체를 생성하여 반환하는 것이다.
        // 반면 StringBuffer 자료형은 값을 변경할 수 있으므로 생성된 값을 언제든지 수정할 수 있다.
    }
}
