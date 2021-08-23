import java.io.*;
import java.util.*;

public class Main {
    static FastReader fastReader = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static int T, M, N, K;
    static int[][] matrix;
    static int[][] dir = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}}; // 상 하 좌 우
    static boolean[][] visited;

    static void input() {
        M = fastReader.nextInt();
        N = fastReader.nextInt();
        K = fastReader.nextInt();
        matrix = new int[N][M];
        visited = new boolean[N][M];
        for (int k = 0; k < K; k++) {
            int y = fastReader.nextInt(), x = fastReader.nextInt();
            matrix[x][y] = 1;
        }
    }

    static void dfs(int x, int y) {
        visited[x][y] = true;

        for (int k = 0; k < 4; k++) {
            int nx = x + dir[k][0];
            int ny = y + dir[k][1];

            if (nx < 0 || ny < 0 || nx >= N || ny >= M) continue;
            if (visited[nx][ny]) continue;
            if (matrix[nx][ny] < 1) continue;

            dfs(nx, ny);
        }
    }

    static void pro() {
        int count = 0;
        for (int x = 0; x < N; x++) {
            for (int y = 0; y < M; y++) {
                if (matrix[x][y] > 0 && !visited[x][y]) {
                    count++;
                    dfs(x, y);
                }
            }
        }
        System.out.println(count);
    }

    public static void main(String[] args) {
        T = fastReader.nextInt();
        for (int i = 0; i < T; i ++) {
            input();
            pro();
        }
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
