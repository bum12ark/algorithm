import java.io.*;
import java.util.*;

public class Main {
    static FastReader fastReader = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static void input() {
        N = fastReader.nextInt();
        S = fastReader.nextInt();
        nums = new int[N];
        for (int i = 0; i < N; i++) nums[i] = fastReader.nextInt();

    }

    static int N, S, ans;
    static int[] nums;

    static void recFunc(int k, int value) {
        if (k == N) {
            if (value == S) ans++;
            return;
        }

        recFunc(k + 1, value + nums[k]);
        recFunc(k + 1, value);
    }

    public static void main(String[] args) {
        input();
        recFunc(0, 0);
        if (S == 0) {
            ans--;
        }
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
