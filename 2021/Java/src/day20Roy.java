import java.util.Scanner;
import java.util.concurrent.TimeUnit;
public class day20Roy {
    // 3x3 pixel

    public static void main(String[] args) {
        // TODO Auto-generated method stub
        Scanner input = new Scanner(System.in);
        char[] algorithm = input.nextLine().toCharArray();
        long startTime = System.nanoTime();
        char[][] image = new char[0][0];
        input.nextLine();
        while (!input.hasNextInt()) {
            char[][] tmpArray = new char[image.length + 1][];
            System.arraycopy(image, 0, tmpArray, 0, image.length);
            tmpArray[image.length] = input.nextLine().toCharArray();
            image = tmpArray;
        }
        char[][] enhancedImage = image;
        boolean borderFlash = algorithm[0] == '#' && algorithm[algorithm.length - 1] == '.';
        boolean borderStaticOn = algorithm[0] == '#' && algorithm[algorithm.length - 1] == '#';
        for (int i = 0; i < 50; i++) {
            if (borderStaticOn && i != 0) {
                enhancedImage = increaseBorders(enhancedImage, true);
                enhancedImage = enhance(enhancedImage, algorithm, true);
            } else if (borderFlash) {
                enhancedImage = increaseBorders(enhancedImage, i % 2 == 1);
                enhancedImage = enhance(enhancedImage, algorithm, i % 2 == 1);
            } else {
                enhancedImage = increaseBorders(enhancedImage, false);
                enhancedImage = enhance(enhancedImage, algorithm, false);
            }
        }
        int count = 0;
        for (int i = 0; i < enhancedImage.length; i++)
            for (int j = 0; j < enhancedImage[i].length; j++)
                if (enhancedImage[i][j] == '#')
                    count++;
        System.out.print(count);
        long endTime = System.currentTimeMillis();
        long timeElapsed = (endTime - startTime);
        System.out.println("\nRun time (in ms): " + timeElapsed);
    }

    public static char[][] enhance(char[][] image, char[] algorithm, boolean borderIsFlashed) {
        // TODO Auto-generated method stub
        if (image != null && algorithm != null) {
            char[][] newImage = new char[image.length][image[0].length];
            for (int i = 0; i < image.length; i++)
                for (int j = 0; j < image[i].length; j++)
                    newImage[i][j] = image[i][j];
            for (int x = 0; x < image.length; x++) {
                for (int y = 0; y < image[x].length; y++) {
                    newImage[x][y] = algorithm[getIndex(image, x, y, borderIsFlashed)];
                }
            }
            return newImage;
        }
        return null;
    }

    public static int getIndex(char[][] image, int x, int y, boolean borderFlash) {
        if (image != null && x >= 0 && x < image.length && y >= 0 && y < image[x].length) {
            int index = 0;
            for (int i = -1; i < 2; i++) {
                for (int j = -1; j < 2; j++) {
                    index *= 2;
                    if (!(i == -1 && x == 0) && !(i == 1 && x == image.length - 1) && !(j == -1 && y == 0) && !(j == 1 && y == image[x].length - 1)) {
                        if (image[x + i][y + j] == '#')
                            index += 1;
                    } else if (borderFlash)
                        index += 1;
                }
            }
            return index;
        }
        return -1;
    }

    public static char[][] increaseBorders(char[][] image, boolean borderFlash) {
        // TODO Auto-generated method stub
        if (image != null) {
            char[][] newImage = new char[image.length + 2][image[0].length + 2];
            for (int i = 0; i < newImage.length; i++) {
                for (int j = 0; j < newImage[i].length; j++) {
                    if (i == 0 || i == newImage.length - 1 || j == 0 || j == newImage[0].length - 1) {
                        if (borderFlash) {
                            newImage[i][j] = '#';
                        } else
                            newImage[i][j] = '.';
                    } else
                        newImage[i][j] = image[i - 1][j - 1];
                }
            }
            return newImage;
        }
        return new char[1][1];
    }
}

