import java.io.*;
import java.util.*;

public class Main {
    static FastReader fastReader = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static int N, M; // 레슨의 수, 녹화할 총 블루레이 개수
    static int[] lessons; // 레슨의 길이

    static void input() {
        N = fastReader.nextInt();
        M = fastReader.nextInt();
        lessons = new int[N];
        for (int i = 0; i < N; i++) lessons[i] = fastReader.nextInt();
    }

    static boolean determination(int minute) {
        int sum = 0, cnt = 1;
        for (int i = 0; i < N; i++) {
            int candidate = sum + lessons[i];
            if (candidate <= minute) {
                sum += lessons[i];
            } else {
                cnt += 1;
                sum = lessons[i];
            }
        }
        return cnt <= M;
    }

    static void process() {
        int left = Arrays.stream(lessons).max().getAsInt(), right = right = 1_000_000_000, ans = 0;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (determination(mid)) {
                ans = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
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
