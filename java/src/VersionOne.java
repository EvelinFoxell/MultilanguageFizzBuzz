/**
 * A simple FizzBuzz in Java
 * Created by Evelin on 2017-01-27.
 */
public class VersionOne {
    public static void main(String[] ignored){
        StringBuilder builder = new StringBuilder(10);
        for(int i = 1; i <= 100; i++){
            if(i % 3 == 0) builder.append("Fizz");
            if(i % 5 == 0) builder.append("Buzz");
            if(builder.length() == 0) builder.append(i);
            System.out.println(builder.toString());
            builder.setLength(0);
        }
    }
}
