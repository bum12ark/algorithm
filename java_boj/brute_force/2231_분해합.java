
import java.io.*;
import java.util.*;

/**
 * link: https://www.acmicpc.net/problem/2231
 * 
 * 2231_분해합
 */
public class Main {
    static FastReader fastReader = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static int N, answer;

    static void input() {
        N = fastReader.nextInt();
    }

    static int getDigitsSum(int num) {
        int sum = 0;
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }

    static void process() {
        for (int candidate = 1; candidate <= N; candidate++) {
            int digitsSum = getDigitsSum(candidate);

            if (candidate + digitsSum == N) {
                answer = candidate;
                return;
            }
        }
    }

    public static void main(String[] args) {
        input();
        process();
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
