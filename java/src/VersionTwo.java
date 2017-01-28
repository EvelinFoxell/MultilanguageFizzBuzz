import java.util.stream.IntStream;

/**
 * A second version of how to make a FizzBuzz
 * Created by Evelin on 2017-01-27.
 */
public class VersionTwo {
    public static void main(String[] ignored) {
        IntStream.range(1, 100).forEach(number -> {
            String answer = "";
            if(number %3 ==0) answer = answer + "Fizz";
            if(number %5 ==0) answer = answer + "Buzz";
            if(answer.length() == 0) answer = String.valueOf(number);
            System.out.println(answer);
        });
    }
}
