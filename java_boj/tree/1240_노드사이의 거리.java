

import java.io.*;
import java.util.*;

/**
 * link: https://www.acmicpc.net/problem/1240
 *
 * 1240_노드사이의 거리
 *
 */
public class Main {
    static FastReader fastReader = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static class Edge {
        int node;
        int distance;

        public Edge(int node, int distance) {
            this.node = node;
            this.distance = distance;
        }

        @Override
        public String toString() {
            return "[" + node + ", " + distance + "]";
        }
    }

    static int N, M; // 노드의 개수, 입력 받을 두 노드 사이의 거리 수
    static Map<Integer, List<Edge>> tree = new HashMap<>(); // {노드, 거리}
    static int[][] question;
    static boolean[] visited;
    static int[] dist;

    static void input() {
        N = fastReader.nextInt();
        M = fastReader.nextInt();
        visited = new boolean[N + 1];
        dist = new int[N + 1];

        for (int i = 1; i <= N; i++) {
            tree.put(i, new ArrayList<>());
        }

        for (int i = 1; i < N; i++) {
            int v1 = fastReader.nextInt();
            int v2 = fastReader.nextInt();
            int distance = fastReader.nextInt();
            tree.get(v1).add(new Edge(v2, distance));
            tree.get(v2).add(new Edge(v1, distance));
        }

        question = new int[M][2];
        for (int m = 0; m < M; m++) {
            question[m][0] = fastReader.nextInt();
            question[m][1] = fastReader.nextInt();
        }
    }

    static void dfs(int vertex) {
        visited[vertex] = true;

        for (Edge edge : tree.get(vertex)) {
            int distance = edge.distance;
            int adj = edge.node;
            if (!visited[adj]) {
                visited[adj] = true;
                dist[adj] = dist[vertex] + distance;
                dfs(adj);
            }
        }
    }

    static void solution() {
        for (int m = 0; m < M; m++) {
            for (int i = 1; i <= N; i++) dist[i] = 0;
            for (int i = 1; i <= N; i++) visited[i] = false;
            dfs(question[m][0]);
            System.out.println(dist[question[m][1]]);
        }
    }

    public static void main(String[] args) {
        input();
        solution();
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