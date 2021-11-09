

import java.io.*;
import java.util.*;

/**
 * link: https://www.acmicpc.net/problem/14267
 *
 * 14267_회사 문화 1
 *
 */
public class Main {
    static FastReader fastReader = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static int N, M;
    static Map<Integer, List<Integer>> child = new HashMap<>();
    static int[] compliment; // 직원 별로 칭찬을 받은 횟수

    static void input() {
        N = fastReader.nextInt();
        M = fastReader.nextInt();
        compliment = new int[N + 1];

        // 그래프 초기화
        for (int index = 1; index <= N; index++) child.put(index, new ArrayList<>());
        for (int vertex = 1; vertex <= N; vertex++) {
            int parent = fastReader.nextInt();
            if (parent != -1) {
                child.get(parent).add(vertex);
            }
        }

        // 칭찬 횟수 초기화
        for (int index = 0; index < M; index++) {
            int i = fastReader.nextInt();
            int w = fastReader.nextInt();
            compliment[i] += w;
        }
    }

    static void dfs(int vertex) {
        for (int adj : child.get(vertex)) {
            compliment[adj] += compliment[vertex];
            dfs(adj);
        }
    }

    static void process() {
        // 1번 정점 부터 그래프 탐색 시작
        dfs(1);

        // 정답 호출
        for (int index = 1; index <= N; index++) {
            sb.append(compliment[index]).append(" ");
        }
    }

    public static void main(String[] args) {
        input();
        process();
        System.out.println(sb);
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