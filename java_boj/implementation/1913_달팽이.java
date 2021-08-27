import java.io.*;
import java.util.*;

/**
 * 1913 - 달팽이 (시물레이션)
 * - 아래 -> 오른쪽 -> 위 -> 왼쪽 순으로 이동
 * - 움직일 수 있는 경우 if 이동 else 방향전환
 * - loop : 칸의 개수 만큼
 */
public class Main {
    static FastReader fastReader = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static int N, target;
    static int[][] snail;
    static int[][] direction = new int[][] {{1, 0}, {0, 1}, {-1, 0}, {0, -1}}; // 하, 우, 상, 좌 순으로 이동

    static void input() {
        N = fastReader.nextInt();
        target = fastReader.nextInt();
        snail = new int[N][N];
    }

    static boolean isMovable(int x, int y) {
        if (x < 0 || y < 0 || x >= N || y >= N) return false;
        return snail[x][y] <= 0;
    }

    static void setSnail() {
        int remainCnt = N * N;
        int x = -1, y = 0, d = 0;

        while (remainCnt-- > 0) {
            int nextX = x + direction[d][0];
            int nextY = y + direction[d][1];

            while (!isMovable(nextX, nextY)) {
                d = (d + 1) % 4;
                nextX = x + direction[d][0];
                nextY = y + direction[d][1];
            }

            snail[nextX][nextY] = remainCnt + 1;
            x = nextX; y = nextY;
        }
    }

    static void printAns() {
        int posX = 0, posY = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                int val = snail[i][j];
                if (val == target) {
                    posX = i + 1; posY = j + 1;
                }
                sb.append(val).append(" ");
            }
            sb.append("\n");
        }
        sb.append(posX).append(" ").append(posY);

        System.out.println(sb);
    }

    static void process() {
        setSnail();
        printAns();
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