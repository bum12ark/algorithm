import java.io.*;
import java.util.*;

/**
 * link: https://www.acmicpc.net/problem/1912
 *
 * 1912_연속합
 */
public class Main {
    static FastReader fastReader = new FastReader();

    static int n; // 수열의 길이
    static int[] sequences;
    static int[] dp;

    static void input() {
        n = fastReader.nextInt();
        sequences = new int[n];
        dp = new int[n];
        for (int i = 0; i < n; i++) {
            sequences[i] = fastReader.nextInt();
            dp[i] = sequences[i];
        }
    }

    static int process() {
        for (int index = 1; index < sequences.length; index++) {
            if (dp[index - 1] > 0) dp[index] += dp[index - 1];
        }
        return Arrays.stream(dp).max().getAsInt();
    }

    public static void main(String[] args) {
        input();
        int answer = process();
        System.out.println(answer);
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
