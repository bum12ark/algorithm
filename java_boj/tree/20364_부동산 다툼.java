

import java.io.*;
import java.util.*;

/**
 * link: https://www.acmicpc.net/problem/20364
 *
 * 20364_부동산 다툼
 *
 */
public class Main {
    static FastReader fastReader = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static int N, Q;
    static int[] wantLand;
    static boolean[] visited;

    static void input() {
        N = fastReader.nextInt();
        Q = fastReader.nextInt();
        visited = new boolean[N + 1];
        wantLand = new int[Q];
        for (int i = 0; i < Q; i++) wantLand[i] = fastReader.nextInt();
    }


    static void solution() {
        for (int land : wantLand) {
            int node = land; // 부모 노드들을 탐색하기 위한 변수
            int stop = 0; // 점유된 땅을 찾기 위한 변수
            while (node > 0) {
                if (visited[node]) {
                    stop = node;
                }
                node /= 2;
            }
            if (stop == 0) visited[land] = true;
            System.out.println(stop);
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