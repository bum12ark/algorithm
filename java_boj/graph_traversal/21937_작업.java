import java.io.*;
import java.util.*;

/**
 * link: https://www.acmicpc.net/problem/21937
 * 
 * 21937 작업
 */
public class Main {
    static FastReader fastReader = new FastReader();
    static StringBuffer sb = new StringBuffer();

    static int N, M, X; // 작업할 개수, 작업 순서 정보, 끝내야 하는 작업
    static int answer;
    static Map<Integer, List<Integer>> graph = new HashMap<>();
    static boolean[] visited;

    static void input() {
        N = fastReader.nextInt();
        M = fastReader.nextInt();

        visited = new boolean[N + 1];
        for (int i = 1; i <= N; i++) {
            graph.put(i, new ArrayList<>());
        }
        for (int i = 0; i < M; i++) {
            int from = fastReader.nextInt();
            int to = fastReader.nextInt();
            graph.get(to).add(from);
        }
        X = fastReader.nextInt();
    }

    static void dfs(int node) {
        answer++;

        visited[node] = true;
        for (int adj : graph.get(node)) {
            if (visited[adj]) continue;
            dfs(adj);
        }
    }

    static void process() {
        dfs(X);
        System.out.println(answer - 1);
    }

    public static void main(String[] args) {
        input();
        process();
    }

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
