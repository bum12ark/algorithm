import java.io.*;
import java.util.*;

public class Main {
    static FastReader fastReader = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static void input() {
        N = fastReader.nextInt();
        column = new int[N + 1];
    }

    static int N, ans;
    static int[] column;

    static boolean validityCheck(int row, int col) {
        // 이전 로우들에 대해 validation check
        for (int prevRow = 1; prevRow < row; prevRow++) {
            int prevColumn = column[prevRow];
            if (prevColumn == col) { // 세로 체크
                return false;
            }
            if (Math.abs(prevRow - row) == Math.abs(prevColumn - col)) { // 대각선 체크
                return false;
            }
        }
        return true;
    }

    static void recFunc(int row) {
        if (row == N + 1) {
            ans++;
            return;
        }
        for (int col = 1; col <= N; col++) {
            column[row] = col;
            if (validityCheck(row, col)) {
                recFunc(row + 1);
            }
            column[row] = 0;
        }
    }

    public static void main(String[] args) {
        input();
        recFunc(1);
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
