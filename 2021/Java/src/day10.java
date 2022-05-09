import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.math.BigInteger;
import java.util.*;

public class day10 {

    public static void main (String[] args) throws IOException {
        String data ="""
        [({(<(())[]>[[{[]{<()<>>
        [(()[<>])]({[<{<<[]>>(
        {([(<{}[<>[]}>{[]{[(<()>
        (((({<>}<{<{<>}{[]{[]{}
        [[<[([]))<([[{}[[()]]]
        [{[{({}]{}}([{[{{{}}([]
        {<[[]]>}<{[{[{[]{()[[[]
        [<(<(<(<{}))><([]([]()
        <{([([[(<>()){}]>(<<{{
        <{([{{}}[<[[[<>{}]]]>[]]
        """;


        BufferedReader br = new BufferedReader(new FileReader("inputs/day 10 "));


        Deque<String> chunk = new ArrayDeque<>();

        BigInteger count = BigInteger.ZERO;
        List<BigInteger> validSums = new ArrayList<>();


        String line;
        while ((line = br.readLine()) != null) {
        //for (String line : data.split("\n")) {
            String[] charArr = line.trim().split("");

            boolean valid = true;

            chunk = new ArrayDeque<>();

            forLoop:
            for(String c : charArr) {
                switch (c) {
                    case "(":
                        chunk.push(c);
                        break;
                    case "[":
                        chunk.push(c);
                        break;
                    case "{":
                        chunk.push(c);
                        break;
                    case "<":
                        chunk.push(c);
                        break;
                    case ")":
                        if (!chunk.peek().equals("(")) {
                            count = count.add(new BigInteger("3"));
                            valid = false;
                            break forLoop;
                        }
                        chunk.pop();
                        break;

                    case "]":
                        if (!chunk.peek().equals("[")) {
                            count = count.add(new BigInteger("57"));
                            valid = false;
                            break forLoop;
                        }
                        chunk.pop();
                        break;
                    case "}":
                        if (!chunk.peek().equals("{")) {
                            count = count.add(new BigInteger("1197"));
                            valid = false;
                            break forLoop;
                        }
                        chunk.pop();
                        break;
                    case ">":
                        if (!chunk.peek().equals("<")) {
                            count = count.add(new BigInteger("25137"));
                            valid = false;
                            break forLoop;
                        }
                        chunk.pop();
                        break;
                }

            }
            if (valid) {
                BigInteger countValid = BigInteger.ZERO;
                while (chunk.size() > 0) {
                    String s = chunk.pop();
                    countValid = countValid.multiply(new BigInteger("5"));
                    switch (s) {
                        case "(":
                            countValid = countValid.add(new BigInteger("1"));
                            break;
                        case "[":
                            countValid = countValid.add(new BigInteger("2"));
                            break;
                        case "{":
                            countValid = countValid.add(new BigInteger("3"));
                            break;
                        case "<":
                            countValid = countValid.add(new BigInteger("4"));
                            break;
                    }
                }
                validSums.add(countValid);
            }
        }

        Collections.sort(validSums);

        System.out.println("Part 1: " + count);
        System.out.println("Part 2: " + validSums.get(validSums.size()/ 2));

    }
}
