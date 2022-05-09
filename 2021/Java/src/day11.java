import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;

public class day11 {

    public static final int HEIGHT = 10;
    public static final int WIDTH = 10;


    public static void main (String[] args) throws IOException {

        String data ="""
        5483143223
        2745854711
        5264556173
        6141336146
        6357385478
        4167524645
        2176841721
        6882881134
        4846848554
        5283751526
        """;

        BufferedReader br = new BufferedReader(new FileReader("inputs/day 11"));

        int[] map = new int[HEIGHT * WIDTH];

        int i = 0;

        String line;
        while ((line = br.readLine()) != null) {
        //for (String line : data.split("\n")) {
            for (String num : line.trim().split("")){
                map[i] = Integer.parseInt(num);
                i++;
            }
        }
        for (int j = 0; j < 1000; j++){
            for (int y = 0; y < HEIGHT; y++) {
                for (int x = 0; x < WIDTH; x++){
                    map[y * WIDTH + x]++;
                }
            }

            boolean[] flashed = new boolean[WIDTH * HEIGHT];
            Arrays.fill(flashed, false);
            boolean hasFlashed = true;
            while (hasFlashed) {
                hasFlashed = false;
                for (int y = 0; y < HEIGHT; y++){
                    for (int x = 0; x < WIDTH; x++) {
                        if (checkFlash(map, flashed, x, y)) {
                            hasFlashed = true;
                        }
                    }
                }
            }
            int flashes = 0;
            for (int y = 0; y < HEIGHT; y++){
                for (int x = 0; x < WIDTH; x++){
                    if (map[y * WIDTH + x] > 9){
                        map[y * WIDTH + x] = 0;
                        flashes++;
                    }
                }
            }
            if(flashes >= 100){
                System.out.println(flashes);
                System.out.println(j + 1);
                System.exit(0);
            }
        }
        //System.out.print (flashes);
    }
    private static boolean checkFlash(int[] map, boolean[] flashed, int x, int y){
        int state = map[y * WIDTH + x];

        if (!flashed[y * WIDTH + x] && state > 9) {
            flashed[y * WIDTH + x] = true;

            if (x < WIDTH - 1)   map[y * WIDTH + x + 1]++;
            if (x > 0)           map[y * WIDTH + x - 1]++;
            if (y < HEIGHT -1)   map[(y + 1) * WIDTH + x]++;
            if (y > 0)           map[(y - 1) * WIDTH + x]++;

            if ( x < WIDTH - 1 && y < HEIGHT -1) map[(y + 1) * WIDTH + x + 1]++;
            if ( x < WIDTH - 1 && y > 0)         map[(y - 1) * WIDTH + x + 1]++;
            if ( x > 0 && y < HEIGHT -1)         map[(y + 1) * WIDTH + x - 1]++;
            if ( x > 0  && y > 0)                map[(y - 1) * WIDTH + x - 1]++;

            return true;
        }
        return false;
    }
}
