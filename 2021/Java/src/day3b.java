import Bingo.BingoBoard;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;

public class day3b {


    public static String getValue(List<String> newData, String selectCriteria, boolean keepMost) {
        int i = 0;

        while (newData.size() > 1) {
            int positive = 0;
            int negative = 0;


            for (String line : newData) {
                String[] lineArr = line.split("");
                String s = lineArr[i];
                if (s.equals("1")) {
                    positive++;
                } else {
                    negative++;
                }
            }

            String keepCriteria = selectCriteria;

            if (positive > negative) {
                if (keepMost) {
                    keepCriteria = "1";
                } else {
                    keepCriteria = "0";
                }
            } else if (positive < negative) {
                if (keepMost) {
                    keepCriteria = "0";
                } else {
                    keepCriteria = "1";
                }
            }

            List<String> keepList = new ArrayList<>();

            for (String line : newData) {
                String[] lineArr = line.split("");
                String val = lineArr[i];
                if (val.equals(keepCriteria)) {
                    keepList.add(line);
                }
            }
            newData = keepList;
            i++;
        }
        return newData.get(0);
    }

    public static void main(String[] args) throws IOException {
        String data = """              
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

        BufferedReader br = new BufferedReader(new FileReader("inputs/day 3 "));

        List<String> newData = new ArrayList<>();

        String line;
        while ((line = br.readLine()) != null){
        //for (String line : data.split("\n")) {
            newData.add(line);
        }

        String oxygenGenerator = getValue(newData, "1", true);
        String CO2scrubber = getValue(newData, "0", false);

        BigInteger oxygenGeneratorNumber = new BigInteger(oxygenGenerator, 2);
        BigInteger CO2scrubberNumber = new BigInteger(CO2scrubber, 2);



        System.out.print(oxygenGeneratorNumber.intValue() * CO2scrubberNumber.intValue());

    }
}
