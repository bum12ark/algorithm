import java.io.*;
import java.util.*;

/**
 * link: https://www.acmicpc.net/problem/14467
 *
 * 14467 - 소가 길을 건너간 이유
 */
public class Main {
    static FastReader fastReader = new FastReader();

    static int N;
    static int[] observation;

    static void input() {
        N = fastReader.nextInt();
        observation = new int[N + 1];
        for (int i = 0; i < N + 1; i++) observation[i] = -1;
    }

    static void process() {
        int ans = 0;
        while (N-- > 0) {
            int cow = fastReader.nextInt();
            int location = fastReader.nextInt();

            int prevLoc = observation[cow];

            if (prevLoc == -1) {
                observation[cow] = location;
                continue;
            }

            if (prevLoc != location) {
                ans += 1;
                observation[cow] = location;
            }
        }
        System.out.println(ans);
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