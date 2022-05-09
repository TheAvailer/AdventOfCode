import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.sql.SQLOutput;

public class day2 {


    public static void main (String[] args) throws IOException {
        String data = """
        forward 5
        down 5
        forward 8
        up 3
        down 8
        forward 2
        """;

        BufferedReader br = new BufferedReader((new FileReader("inputs/day 2 ")));

        int depth = 0;
        int horizontal = 0;
        int aim = 0;

        String line;
        while ((line = br.readLine()) != null)
        {
        //for (String line : data.split("\n")) {
            String[] arg= line.split(" ");
            String cmd = arg[0];
            int amount = Integer.parseInt(arg[1]);
            switch (cmd) {
                case "forward" :
                    horizontal += amount;
                    depth += aim * amount;
                    break;
                case "backward":
                    horizontal -= amount;
                    break;
                case "down":
                    aim += amount;
                    break;
                case "up":
                    aim -= amount;
                    break;
            }
        }
        System.out.println(depth *horizontal);
    }
}
