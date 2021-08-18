import java.io.*;
import java.util.*;

public class Main {
    static FastReader fastReader = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static int N, K; // 주전자의 개수, 친구들의 수
    static int[] makgeolli;

    static void input() {
        N = fastReader.nextInt();
        K = fastReader.nextInt();
        makgeolli = new int[N];
        for (int i = 0; i < N; i++) makgeolli[i] = fastReader.nextInt();
    }

    static boolean determination(int ml) {
        int sum = 0, cnt = 0;
        for (int volume : makgeolli) {
            cnt += volume / ml;
        }
        return cnt >= K;
    }

    static void process() {
        int left = 0, right = Integer.MAX_VALUE, ans = 0;
        while (left <= right) {
            int mid = left + (right - left) / 2;
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
