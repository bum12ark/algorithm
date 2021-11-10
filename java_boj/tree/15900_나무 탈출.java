

import java.io.*;
import java.util.*;

/**
 * link: https://www.acmicpc.net/problem/15900
 *
 * 15900_나무 탈출
 *
 */
public class Main {
    static FastReader fastReader = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static int N, ans;
    static Map<Integer, List<Integer>> tree = new HashMap<>();

    static void input() {
        N = fastReader.nextInt();

        for (int i = 1; i <= N; i++) {
            tree.put(i, new ArrayList<>());
        }

        for (int i = 0; i < N - 1; i++) {
            int parent = fastReader.nextInt();
            int child = fastReader.nextInt();
            tree.get(parent).add(child);
            tree.get(child).add(parent);
        }
    }

    static void dfs(int x, int parent, int depth) {
        if (tree.get(x).size() == 1) {
            ans += depth;
        }

        for (int adj : tree.get(x)) {
            if (adj == parent) continue;
            dfs(adj, x, depth + 1);
        }
    }

    static void solution() {
        dfs(1, -1, 0);
        if (ans % 2 == 0) {
            System.out.println("No");
        } else {
            System.out.println("Yes");
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