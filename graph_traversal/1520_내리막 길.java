import java.io.*;
import java.util.*;

/**
 * graph + dp
 */
public class Main {
    static FastReader fastReader = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static int R, C; // 세로의 크기, 가로의 크기
    static int[][] matrix, dp;
    static int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}}; // 상 하 좌 우

    static void input() {
        R = fastReader.nextInt();
        C = fastReader.nextInt();

        matrix = new int[R][C];
        dp = new int[R][C];
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                matrix[r][c] = fastReader.nextInt();
                dp[r][c] = -1;
            }
        }
    }

    static int dfs(int x, int y) {
        if (x == R - 1 && y == C - 1) {
            return 1;
        }

        if (dp[x][y] == -1) {
            dp[x][y] = 0;
            for (int[] direction : directions) {
                int nextX = direction[0] + x;
                int nextY = direction[1] + y;

                if (nextX < 0 || nextY < 0 || nextX >= R || nextY >= C) continue;
                if (matrix[x][y] > matrix[nextX][nextY]) {
                    dp[x][y] += dfs(nextX, nextY);
                }
            }
        }

        return dp[x][y];
    }

    static void process() {
        dfs(0, 0);
        System.out.println(dp[0][0]);
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
