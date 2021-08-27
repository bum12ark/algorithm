import java.io.*;
import java.util.*;

/**
 * link: https://www.acmicpc.net/problem/14502
 *
 * 14502 - 연구소
 * 1. 3개의 벽을 세우는 경우 (완전탐색) => bC3
 * 2. Multisource BFS 를 사용하여 바이러스로 부터 안전한 구역 확인 => O(N * M)
 */
public class Main {
    static FastReader fastReader = new FastReader();

    static class Pos {
        int x, y;

        public Pos(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static int N, M, ans;
    static int[][] map;
    static boolean[][] visited;
    static int[][] direction = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    static List<Pos> blankList = new ArrayList<>();

    static final int BLANK = 0, WALL = 1, VIRUS = 2;

    static void input() {
        N = fastReader.nextInt();
        M = fastReader.nextInt();
        map = new int[N][M];
        for (int i = 0; i < N; i++) for (int j = 0; j < M; j++) map[i][j] = fastReader.nextInt();

        visited = new boolean[N][M];
    }

    static void bfs() {
        Queue<Pos> queue = new LinkedList<>();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (map[i][j] == VIRUS) {
                    visited[i][j] = true;
                    queue.add(new Pos(i, j));
                }
                visited[i][j] = false;
            }
        }

        while (!queue.isEmpty()) {
            Pos pos = queue.poll();
            int x = pos.x, y = pos.y;
            for (int[] dir : direction) {
                int nextX = x + dir[0];
                int nextY = y + dir[1];

                if (nextX < 0 || nextY < 0 || nextX >= N || nextY >= M) continue;
                if (visited[nextX][nextY]) continue;
                if (map[nextX][nextY] != BLANK) continue;

                visited[nextX][nextY] = true;
                queue.add(new Pos(nextX, nextY));
            }
        }

        int cnt = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (map[i][j] == BLANK && !visited[i][j]) cnt++;
            }
        }
        ans = Math.max(ans, cnt);
    }

    static void buildingWall(int idx, int selectedCnt) {
        if (selectedCnt == 3) {
            bfs();
            return;
        }
        if (idx >= blankList.size()) return;

        Pos pos = blankList.get(idx);
        int x = pos.x, y = pos.y;

        map[pos.x][pos.y] = WALL;
        buildingWall(idx + 1, selectedCnt + 1);
        map[pos.x][pos.y] = BLANK;
        buildingWall(idx + 1, selectedCnt);
    }

    static void process() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (map[i][j] == BLANK) {
                    blankList.add(new Pos(i, j));
                }
            }
        }

        // 벽을 3개 세우는 모든 방법 확인!
        buildingWall(0, 0);

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