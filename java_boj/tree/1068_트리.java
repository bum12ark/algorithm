
import java.io.*;
import java.util.*;

/**
 * link: https://www.acmicpc.net/problem/1068
 *
 * 1068_트리
 *
 */
public class Main {
    static FastReader fastReader = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static int n, erased, root;
    static Map<Integer, List<Integer>> child = new HashMap<>();
    static int[] leaf; // x 를 root 로 하는 subtree 에 있는 단말 노드의 개수

    static void input() {
        n = fastReader.nextInt();
        leaf = new int[n];
        for (int i = 0; i < n; i++) child.put(i, new ArrayList<>());
        for (int i = 0; i < n; i++) {
            int parent = fastReader.nextInt();
            if (parent == -1) {
                root = i;
            } else {
                child.get(parent).add(i);
            }
        }
        erased = fastReader.nextInt();
    }

    static void dfs(int x) {
        if (child.get(x).isEmpty()) { // 리프 노드라면
            leaf[x] = 1;
        }

        for (int adj : child.get(x)) {
            dfs(adj);
            leaf[x] += leaf[adj];
        }
    }

    static void solution() {
        for (int i = 0; i < n; i++) {
            if (child.get(i).contains(erased)) {
                // erased 가 포함된 그래프 삭제
                child.get(i).remove((Integer) erased);
            }
        }

        if (root != erased) {
            dfs(root);
        }
        System.out.println(leaf[root]);
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