import java.io.*;
import java.util.*;

/**
 * link: https://www.acmicpc.net/problem/2579
 *
 * 2579 - 계단 오르기
 */
public class Main {
    static FastReader fastReader = new FastReader();
    static int N, ans;
    static int[] stairs;
    static int[][] dp;

    static void input() {
        N = fastReader.nextInt();
        dp = new int[N + 1][2];
        stairs = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            stairs[i] = fastReader.nextInt();
        }
    }

    static void process() {
        dp[1][0] = 0;
        dp[1][1] = stairs[1];

        if (N >= 2) {
            dp[2][0] = stairs[2];
            dp[2][1] = stairs[1] + stairs[2];
        }

        for (int index = 3; index <= N; index++) {
            dp[index][0] = Math.max(dp[index - 2][0], dp[index - 2][1]) + stairs[index];
            dp[index][1] = dp[index - 1][0] + stairs[index];

        }
        ans = Math.max(dp[N][0], dp[N][1]);
    }

    public static void main(String[] args) {
        input();
        process();
        System.out.println(ans);
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