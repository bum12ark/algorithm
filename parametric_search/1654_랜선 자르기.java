import java.io.*;
import java.util.*;

public class Main {
    static FastReader fastReader = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static int K, N; // 이미 가지고 있는 랜선의 개수, 필요한 랜선의 개수
    static int[] lengths; // 랜선의 길이

    static void input() {
        K = fastReader.nextInt();
        N = fastReader.nextInt();
        lengths = new int[K];
        for (int i = 0; i < K; i++) lengths[i] = fastReader.nextInt();
    }

    static boolean determination(long cut) {
        long sum = 0;
        for (int length : lengths) {
            sum += length / cut;
        }
        return sum >= N;
    }

    static void process() {
        long left = 1, right = Integer.MAX_VALUE, ans = 0;
        while (left <= right) {
            long mid = left + (right - left) / 2;
            if (determination(mid)) {
                ans = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
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
