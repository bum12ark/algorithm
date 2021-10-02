
import java.io.*;
import java.util.*;

/**
 * link: https://www.acmicpc.net/problem/1107
 *
 * 리모컨
 */
public class Main {
    static FastReader fastReader = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static int N, M;
    static boolean[] brokenButtons;
    static final int WATCHING_CHANNEL = 100;

    static void input() {
        N = fastReader.nextInt();
        M = fastReader.nextInt();

        brokenButtons = new boolean[10];
        for (int i = 0; i < M; i++) {
            int brokenButton = fastReader.nextInt();
            brokenButtons[brokenButton] = true;
        }
    }

    static boolean isPress(int num) {
        if (num == 0) {
            return !brokenButtons[num];
        }

        while (num > 0) {
            int button = num % 10;
            if (brokenButtons[button]) return false;
            num /= 10;
        }
        return true;
    }

    static int getLength(int num) {
        return String.valueOf(num).length();
    }

    static int changeEntirely(int num) {
        int maxClick = 500_000;
        for (int i = 0; i <= 1_000_000; i++) {
            if (!isPress(i)) continue;

            int distance = getLength(i) + Math.abs(i - num);
            maxClick = Math.min(maxClick, distance);
        }

         return maxClick;
    }

    static void process() {
        // +/- 버튼으로만 갔을 때의 횟수
        int ans = Math.abs(N - WATCHING_CHANNEL);

        // 수동 채널 변경으로 횟수
        ans = Math.min(ans, changeEntirely(N));

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
