
import java.io.*;
import java.util.*;

/**
 * link: https://www.acmicpc.net/problem/21938
 *
 * 21938 영상처리
 */
public class Main {
    static FastReader fastReader = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static class Pixel {
        int R, G, B;

        public Pixel(int r, int g, int b) {
            R = r;
            G = g;
            B = b;
        }

        public int getAverage() {
            return (R + G + B) / 3;
        }
    }

    static int N, M, T; // 세로, 가로, 경계값
    static Pixel[][] pixels;
    static boolean[][] visited;
    static int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}}; // 상 하 좌 우

    static void input() {
        N = fastReader.nextInt();
        M = fastReader.nextInt();

        pixels = new Pixel[N][M];
        visited = new boolean[N][M];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                int r = fastReader.nextInt();
                int g = fastReader.nextInt();
                int b = fastReader.nextInt();
                pixels[i][j] = new Pixel(r, g, b);
            }
        }

        T = fastReader.nextInt();
    }

    static void dfs(int row, int col) {
        visited[row][col] = true;

        for (int k = 0; k < 4; k++) {
            int nextX = row + directions[k][0];
            int nextY = col + directions[k][1];

            if (nextX < 0 || nextY < 0 || nextX >= N || nextY >= M) continue; // 탐색 가능 범위
            if (visited[nextX][nextY]) continue; // 방문 여부
            if (pixels[nextX][nextY].getAverage() < T) continue; // 픽셀 평균값 -> 새로운 화면

            dfs(nextX, nextY);
        }
    }

    static void process() {
        int answer = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (visited[i][j]) continue;
                if (pixels[i][j].getAverage() < T) continue;

                dfs(i, j);
                answer += 1;
            }
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
