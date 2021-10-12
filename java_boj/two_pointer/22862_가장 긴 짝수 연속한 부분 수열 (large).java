
import java.io.*;
import java.util.*;

/**
 * link: https://www.acmicpc.net/problem/22862
 *
 * 22857_가장 긴 짝수 연속한 부분 수열 (large)
 *
 * */
public class Main {
    static FastReader fastReader = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static int N, K; // 수열의 길이, 삭제할 수 있는 최대 회수
    static int[] S;


    static void input() {
        N = fastReader.nextInt();
        K = fastReader.nextInt();
        S = new int[N];
        for (int i = 0; i < N; i++) {
            S[i] = fastReader.nextInt();
        }
    }

    static void process() {
        int right = 0, eraseCount = 0, answer = 0;
        for (int left = 0; left < N; left++) {
            while (right < N && eraseCount <= K) { // right 포인터 증가
                if (S[right] % 2 != 0) {
                    eraseCount += 1;
                }
                right += 1;
            }

            answer = Math.max(answer, right - left - eraseCount);

            // left 이동에 따른 eraseCount 감소
            if (S[left] % 2 != 0) eraseCount -= 1;
        }

        System.out.println(answer);
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

