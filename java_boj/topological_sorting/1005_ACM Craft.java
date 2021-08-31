import java.io.*;
import java.util.*;

/**
 * link: https://www.acmicpc.net/problem/1005
 *
 * 1005 - ACM Craft
 */
public class Main {
    static FastReader fastReader = new FastReader();

    static int T, N, K; // 테스트 케이스, 건물의 개수, 건설순서규칙
    static int[] time, indegree, done; // 짓는데 걸리는 시간
    static Map<Integer, List<Integer>> graph = new HashMap<>();

    static void input() {
        N = fastReader.nextInt();
        K = fastReader.nextInt();
        indegree = new int[N + 1];
        time = new int[N + 1];
        done = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            time[i] = fastReader.nextInt();
            graph.put(i, new ArrayList<>());
        }

        for (int k = 0; k < K; k++) {
            int in = fastReader.nextInt();
            int out = fastReader.nextInt();
            graph.get(in).add(out);
            indegree[out]++;
        }

    }

    static void solution() {
        Deque<Integer> deque = new LinkedList<>();
        // 제일 앞에 "정렬될 수 있는" 정점 찾기
        for (int i = 1; i <= N; i++) {
            if (indegree[i] == 0) {
                deque.add(i);
                // 제일 앞에 정렬된다는 것은 자기 자신의 시간이 곧 소요시간
                done[i] = time[i];
            }
        }

        // 위상 정렬 순서대로 T_done 계산을 함께 해주기기
        while (!deque.isEmpty()) {
            Integer nextN = deque.poll();
            for (int adj : graph.get(nextN)) {
                // 정점과 연결된 간선 삭제
                indegree[adj]--;
                if (indegree[adj] == 0) {
                    deque.add(adj);
                    // done[adj] = Math.max(done[adj], done[nextN] + time[adj]);
                }
                // indegree 가 0 일 때만 계산한다면 다른 indgree 들에 대한 최대 값 계산을 할 수 없기 때문에
                // if 문 밖에서 계산한다.
                done[adj] = Math.max(done[adj], done[nextN] + time[adj]);
            }
        }
        int W = fastReader.nextInt();
        System.out.println(done[W]);
    }
    public static void main(String[] args) {
        T = fastReader.nextInt();
        for (int t = 0; t < T; t++) {
            input();
            solution();
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