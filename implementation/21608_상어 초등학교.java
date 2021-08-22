import java.io.*;
import java.util.*;

/**
 * 21608 - 상어 초등학교
 */
public class Main {
    static FastReader fastReader = new FastReader();

    static class Pos {
        int x, y;

        public Pos(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static int N;
    static int[][] seats;
    static Map<Integer, Pos> posMap = new HashMap<>();
    static int[][] dir = new int[][] {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    static void input() {
        N = fastReader.nextInt();

        seats = new int[N + 1][N + 1];
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                seats[i][j] = 4;
                if (i == 1 || i == N) seats[i][j] -= 1;
                if (j == 1 || j == N) seats[i][j] -= 1;
            }
        }
    }

    static int getMaxValue(int x, int y) {
        int res = 0;
        for (int i = 0; i < 4; i++) {
            int nextX = x + dir[i][0];
            int nextY = y + dir[i][1];
            if (nextX < 1 || nextY < 1 || nextX > N || nextY > N) continue;

        }
        return 0;
    }

    static void firstCondition(int[] likes) {
        int maxValue = 0, minX = 0, minY = 0;
        Pos maxPos = null;
        for (int i = 0; i < likes.length; i++) {
            if (posMap.containsKey(likes[i])) {
                Pos pos = posMap.get(likes[i]);
                int getValue = getMaxValue(pos.x, pos.y);
                if (maxValue < getValue) {
                    maxPos = new Pos(pos.x, pos.y);
                    maxValue = getValue;
                } else if (maxValue == getValue) {
                    if (minX > pos.x) maxPos = new Pos(pos.x, pos.y);
                    if (minY > pos.y) maxPos = new Pos(pos.x, pos.y);
                }
            }
        }
        if (maxPos == null) {

        }
    }

    static void process() {
        int cnt = N * N;
        int[] likes = new int[4];
        while (cnt-- > 0) {
            int number = fastReader.nextInt();
            for (int i = 0; i < 4; i++) {
                likes[i] = fastReader.nextInt();
            }
            System.out.println(number + ", " + Arrays.toString(likes));
            firstCondition(likes);
        }
    }

    public static void main(String[] args) {
        input();
        process();
    }

    // FastReader
    static class FastReader {
        private BufferedReader br;
        private StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        public FastReader(String s) throws FileNotFoundException {
            br = new BufferedReader(new FileReader(new File(s)));
        }

        public String next() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }

        public long nextLong() {
            return Long.parseLong(next());
        }

        public double nextDouble() {
            return Double.parseDouble(next());
        }

        public String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
}
