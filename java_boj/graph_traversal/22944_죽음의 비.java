import java.io.*;
import java.util.*;

/**
 * link: https://www.acmicpc.net/problem/22944
 *
 * 죽음의 비
 */
public class Main {
    static FastReader fastReader = new FastReader();

    static int N, H, D; // 한변의 길이, 체력, 내구도
    static char[][] maps; // 가로, 세로, 내구도
    static int[][] visited;
    static int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}}; // 상하좌우
    static int[][] distance;

    static class Pos {
        int x, y, strength, durability;

        public Pos(int x, int y, int strength, int durability) {
            this.x = x;
            this.y = y;
            this.strength = strength;
            this.durability = durability;
        }

    }

    static void input() {
        N = fastReader.nextInt();
        H = fastReader.nextInt();
        D = fastReader.nextInt();

        maps = new char[N][N];
        visited = new int[N][N];
        distance = new int[N][N];

        for (int i = 0; i < N; i++) {
            maps[i] = fastReader.nextLine().toCharArray();
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (maps[i][j] == 'E') distance[i][j] = -1;
            }
        }
    }

    static void process(Pos pos) {
        Queue<Pos> queue = new LinkedList<>();
        queue.add(pos);

        while (false == queue.isEmpty()) {
            Pos poll = queue.poll();

            for (int[] direction : directions) {
                int nextX = poll.x + direction[0];
                int nextY = poll.y + direction[1];
                Pos next = new Pos(nextX, nextY, poll.strength, poll.durability);

                if (nextX < 0 || nextY < 0 || nextX >= N || nextY >= N) continue;

                if (maps[nextX][nextY] == 'E') {
                    distance[nextX][nextY] = distance[poll.x][poll.y] + 1;
                    return;
                }

                if (maps[nextX][nextY] == 'U') { // 우산을 듦
                    next.durability = D;
                }

                if (next.durability > 0) {
                    next.durability -= 1;
                } else {
                    next.strength -= 1;
                }

                if (next.strength <= 0) continue;

                // 더 멀리 갈 수 있는 경우에만 방문 처리
                if (visited[nextX][nextY] < next.strength + next.durability) {
                    visited[nextX][nextY] = next.strength + next.durability;
                    distance[nextX][nextY] = distance[poll.x][poll.y] + 1;
                    queue.add(next);
                }
            }
        }
    }

    public static void main(String[] args) {
        input();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (maps[i][j] != 'S') continue;
                process(new Pos(i, j, H, 0));
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (maps[i][j] == 'E') System.out.println(distance[i][j]);
            }
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
            br = new BufferedReader(new FileReader(new java.io.File(s)));
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
