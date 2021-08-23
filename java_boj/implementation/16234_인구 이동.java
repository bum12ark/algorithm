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
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Pos pos = (Pos) o;
            return x == pos.x && y == pos.y;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }

        @Override
        public String toString() {
            return "(" + x + ", " + y + ")";
        }
    }

    static int N, L, R;
    static int[][] A;
    static boolean[][] visited;
    static List<Set<Pos>> unionList = new ArrayList<>();
    static int[][] dir = new int[][] {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    static void input() {
        N = fastReader.nextInt();
        L = fastReader.nextInt();
        R = fastReader.nextInt();
        A = new int[N][N];
        for (int i = 0; i < N; i++) for (int j = 0; j < N; j++) A[i][j] = fastReader.nextInt();
        visited = new boolean[N][N];
    }

    static Set<Pos> bfs(int x, int y) {
        Queue<Integer> queue = new LinkedList<>();
        visited[x][y] = true;
        queue.add(x); queue.add(y);

        Set<Pos> union = new LinkedHashSet<>();
        while (!queue.isEmpty()) {
            x = queue.poll(); y = queue.poll();
            for (int[] _dir : dir) {
                int nextX = x + _dir[0];
                int nextY = y + _dir[1];

                if (nextX < 0 || nextY < 0 || nextX >= N || nextY >= N) continue;
                if (visited[nextX][nextY]) continue;
                if (Math.abs(A[x][y] - A[nextX][nextY]) < L) continue;
                if (Math.abs(A[x][y] - A[nextX][nextY]) > R) continue;

                union.add(new Pos(x, y));
                union.add(new Pos(nextX, nextY));
                visited[nextX][nextY] = true;
                queue.add(nextX); queue.add(nextY);
            }
        }
        return union;
    }

    static int getPopulation(Set<Pos> posSet) {
        int res = 0;
        for (Pos pos : posSet) {
            res += A[pos.x][pos.y];
        }
        return res;
    }

    static boolean isOpen() {
        for (int i = 0; i < N; i++) for (int j = 0; j < N; j++) visited[i][j] = false;

        int cnt = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (visited[i][j]) continue;
                // 탐색 시작
                Set<Pos> posSet = bfs(i, j);
                // 인구 이동이 발생할 수 없다면 continue
                if (posSet.isEmpty()) continue;
                unionList.add(posSet);
                cnt += 1;
            }
        }

        return cnt > 0;
    }

    static void process() {
        int ans = 0;
        while (isOpen()) {
            ans += 1;
            for (Set<Pos> posSet : unionList) {
                int population = getPopulation(posSet);
                int cnt = posSet.size();
                for (Pos pos : posSet) {
                    A[pos.x][pos.y] = population / cnt;
                }
            }
            unionList.clear();
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
