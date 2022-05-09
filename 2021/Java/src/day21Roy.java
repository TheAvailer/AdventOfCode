public class day21Roy {
    public static int[] frequency = {0, 0, 0, 1, 3, 6, 7, 6, 3, 1};

    public static long mostWins (int p1start, int p2start)
    {
        long[] p1wins = new long[1];
        long[] p2wins = new long[1];

        itterate(p1wins, p2wins, 0, p1start, 0, p2start, true);

        if (p1wins[0]<p2wins[0])
            return p2wins[0];
        return p1wins[0];
    }

    public static int nextPos (int pos, int move)
    {
        if (pos+move>10)
            return (pos+move-1)%10+1;
        else
            return pos+move;
    }

    public static void itterate (long[] p1wins, long[] p2wins, int p1score, int p1pos, int p2score, int p2pos, boolean p1Turn) {
        for (int h = 0; h < 1; h++) {
            System.out.println("it"+h);
            for (int a = 3; a < 10; a++) {
                System.out.println("itter"+ (a-3));
                if (p1Turn) {
                    int next1pos = nextPos(p1pos, a);
                    if (p1score + next1pos >= 21)
                        p1wins[0] += frequency[a];
                    else
                        itterate(p1wins, p2wins, p1score + next1pos, next1pos, p2score, p2pos, !p1Turn);
                } else {
                    int next2pos = nextPos(p2pos, a);
                    if (p2score + next2pos >= 21)
                        p2wins[0] += frequency[a];
                    else
                        itterate(p1wins, p2wins, p1score, p1pos, p2score + next2pos, next2pos, !p1Turn);
                }
            }
        }
    }
    public static void main(String[] args){
        System.out.println(mostWins(8,6));
        //716241959649754
        //83056435261277956
    }
}
