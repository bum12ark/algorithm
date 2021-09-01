import java.io.*;
import java.util.*;

/**
 * link: https://www.acmicpc.net/problem/2252
 *
 * 2252 - 줄 세우기
 */
public class Main {
    static FastReader fastReader = new FastReader();
    static StringBuffer sb = new StringBuffer();

    static int n, m;
    static int[] indeg;
    static Map<Integer, List<Integer>> graph = new HashMap<>();

    static void input() {
        n = fastReader.nextInt();
        m = fastReader.nextInt();
        indeg = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            graph.put(i, new ArrayList<>());
        }
        for (int i = 1; i <= m; i++) {
            int in = fastReader.nextInt();
            int out = fastReader.nextInt();
            graph.get(in).add(out);
            indeg[out]++;
        }
    }

    static void solution() {
        Deque<Integer> deque = new LinkedList<>();
        // 제일 앞에 "정렬될 수 있는" 정점 찾기
        for (int i = 1; i <= n; i++) {
            if (indeg[i] == 0) deque.add(i);
        }

        // 정렬될 수 있는 정점이 있다면?
        while (!deque.isEmpty()) {
            Integer nx = deque.poll();
            // 1. 정렬 결과에 추가하기
            sb.append(nx).append(' ');
            // 2. 정점과 연결된 간선 제거하기
            for (int adj : graph.get(nx)) {
                indeg[adj]--;
                // 3. 새롭게 "정렬될 수 있는" 정점
                if (indeg[adj] == 0) deque.add(adj);
            }
        }
        System.out.println(sb);
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