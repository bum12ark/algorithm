import java.io.*;
import java.util.*;

/**
 * 16234 - 인구 이동 (시물레이션)
 *
 * 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
 * 위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
 * 국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.
 * 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
 * 연합을 해체하고, 모든 국경선을 닫는다.
 *
 * [변경점]
 * - set 을 사용하지 않고 list 만으로 해결
 * - list 에 연합을 모두 저장한 뒤 인구 이동 -> 연합이 생성될 경우 인구 이동
 * - 중복 코드, 연산에 대해 변수 또는 메소드로 변경
 *
 * 수행시간 단축! 1144ms -> 652ms
 */
public class Main {
    static FastReader fastReader = new FastReader();

    static class Pos {
        int x, y;

        public Pos(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public String toString() {
            return "(" + x + ", " + y + ")";
        }
    }

    static int N, L, R;
    static int[][] A;
    static boolean[][] visited;
    static int[][] dir = new int[][] {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    static void input() {
        N = fastReader.nextInt();
        L = fastReader.nextInt();
        R = fastReader.nextInt();
        A = new int[N][N];
        for (int i = 0; i < N; i++) for (int j = 0; j < N; j++) A[i][j] = fastReader.nextInt();
        visited = new boolean[N][N];
    }

    static boolean bfs(int x, int y) {
        Queue<Integer> queue = new LinkedList<>();
        visited[x][y] = true;
        queue.add(x); queue.add(y);

        List<Pos> union = new ArrayList<>();
        union.add(new Pos(x, y));

        int population = A[x][y];
        while (!queue.isEmpty()) {
            x = queue.poll(); y = queue.poll();
            for (int[] _dir : dir) {
                int nextX = x + _dir[0];
                int nextY = y + _dir[1];

                if (nextX < 0 || nextY < 0 || nextX >= N || nextY >= N) continue;
                if (visited[nextX][nextY]) continue;
                int differ = Math.abs(A[x][y] - A[nextX][nextY]);
                if (differ < L || differ > R) continue;

                population += A[nextX][nextY];
                union.add(new Pos(nextX, nextY));
                visited[nextX][nextY] = true;
                queue.add(nextX); queue.add(nextY);
            }
        }

        if (union.size() <= 1) return false;

        // 연합이 만들어 졌다면
        populationMove(population, union);
        return true;
    }

    static void populationMove(int population, List<Pos> union) {
        int changedPopulation = population / union.size();
        for (Pos pos : union) {
            A[pos.x][pos.y] = changedPopulation;
        }
    }

    static boolean isOpen() {
        for (int i = 0; i < N; i++) for (int j = 0; j < N; j++) visited[i][j] = false;

        int cnt = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (visited[i][j]) continue;
                // 탐색 시작
                if (!bfs(i, j)) continue;
                cnt += 1;
            }
        }

        return cnt > 0;
    }

    static void process() {
        int ans = 0;
        while (isOpen()) {
            ans += 1;
        }

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
