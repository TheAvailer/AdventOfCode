import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.math.BigInteger;

public class day3 {

    public static void main (String[] args) throws IOException {
        String data ="""              
        00100
        11110
        10110
        10111
        10101
        01111
        00111
        11100
        10000
        11001
        00010
        01010
        """;

        BufferedReader br = new BufferedReader((new FileReader("inputs/day 3 ")));


        String line;

        int[] positiveBits = new int[12];
        int[] negativeBits = new int[12];

        while ((line = br.readLine()) != null){
        //for (String line : data.split("\n")) {
            String[] lineArr = line.split("");
            int i = 0;
            for (String s : lineArr){
                if (s.equals("1")) {
                    positiveBits[i]++;
                }else
                {
                    negativeBits[i]++;
                }
                i++;
            }

        }
        String most ="";
        String least = "";
        for (int i = 0; i < positiveBits.length; i++) {
            if (positiveBits[i] > negativeBits[i]) {
                most += "1";
                least += "0";
            }
            else{
                most += "0";
                least += "1";
            }

        }

        BigInteger mostFrequentNumber = new BigInteger(most, 2);
        BigInteger leastFrequentNumber = new BigInteger(least, 2);


        System.out.println(mostFrequentNumber.intValue() * leastFrequentNumber.intValue() );


    }
}
