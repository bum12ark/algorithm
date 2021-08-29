import java.io.*;
import java.util.*;

/**
 * link: https://www.acmicpc.net/problem/14501
 *
 * 14501 - 퇴사
 * - 상담을 하는 경우 (상담이 가능할 때)
 * - 상담을 하지 않는 경우
 * 재귀를 이용한 완전탐색 문제
 */
public class Main {
    static FastReader fastReader = new FastReader();

    static int N, maxVal;
    static int[] T, P;

    static void input() {
        N = fastReader.nextInt();
        T = new int[N + 1];
        P = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            T[i] = fastReader.nextInt();
            P[i] = fastReader.nextInt();
        }
    }

    static void recFunc(int idx, int pay) {
        if (idx > N) {
            maxVal = Math.max(maxVal, pay);
            return;
        }

        if (idx + T[idx] <= N + 1) { // 상담을 할 수 있는 경우
            recFunc(idx + T[idx], pay + P[idx]);
        }

        // 상담을 하지 않는 경우
        recFunc(idx + 1, pay);
    }

    static void process() {
        recFunc(1, 0);
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