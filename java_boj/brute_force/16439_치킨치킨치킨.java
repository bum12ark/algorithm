import java.io.*;
import java.util.*;

/**
 * link: https://www.acmicpc.net/problem/16439
 *
 * 16439 - 치킨치킨치킨
 */
public class Main {
    static FastReader fastReader = new FastReader();

    static int N, M, maxVal; // 회원의 수, 치킨 종류의 수, 최댓값
    static int[][] preferences; // 선호도
    static boolean[] visited; // 방문 여부

    static void input() {
        N = fastReader.nextInt(); M = fastReader.nextInt();
        visited = new boolean[M];
        preferences = new int[N][M];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                preferences[i][j] = fastReader.nextInt();
            }
        }
    }

    // 선택한 치킨의 종류 중에서 최대 합을 구해 리턴하는 메서드
    static int cal() {
        int res = 0;
        for (int i = 0; i < N; i++) {
            int innerMax = 0;
            for (int j = 0; j < M; j++) {
                if (!visited[j]) continue;
                innerMax = Math.max(innerMax, preferences[i][j]);
            }
            res += innerMax;
        }
        return res;
    }

    static void recFunc(int idx, int selectedCnt) {
        if (selectedCnt >= 3) {
            maxVal = Math.max(maxVal, cal());
            return;
        }
        if (idx >= M) return;

        // 선택 함
        visited[idx] = true;
        recFunc(idx + 1, selectedCnt + 1);
        // 선택하지 않음
        visited[idx] = false;
        recFunc(idx + 1, selectedCnt);
    }

    static void process() {
        recFunc(0, 0);
        System.out.println(maxVal);
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