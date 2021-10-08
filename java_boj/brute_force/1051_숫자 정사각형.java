
import java.io.*;
import java.util.*;

/**
 * link: https://www.acmicpc.net/problem/1051
 *
 * 숫자 정사각형
 */
public class Main {
    static FastReader fastReader = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static int N, M;
    static char[][] rectangle;

    static void input() {
        N = fastReader.nextInt();
        M = fastReader.nextInt();

        rectangle = new char[N][M];
        for (int i = 0; i < N; i++) {
            rectangle[i] = fastReader.nextLine().toCharArray();
        }
    }

    static void process() {
        int minSize = Math.min(N, M);

        int side = 1;
        for (int row = 0; row < N; row++) {
            for (int col = 0; col < M; col++) {
                for (int k = 1; k < minSize; k++) {
                    if (row + k >= N || col + k >= M) continue;

                    if (rectangle[row + k][col] == rectangle[row][col] &&
                            rectangle[row][col + k] == rectangle[row][col] &&
                            rectangle[row +k][col + k] == rectangle[row][col]) {
                        side = Math.max(side, k + 1);
                    }
                }
            }
        }

        int result = side * side;
        System.out.println(result);
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
