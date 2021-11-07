

import java.io.*;
import java.util.*;

/**
 * link: https://www.acmicpc.net/problem/1991
 *
 * 1991_트리 순회
 *
 */
public class Main {
    static FastReader fastReader = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static int n;
    static int[][] childs;

    static void input() {
        n = fastReader.nextInt();
        childs = new int[30][2];
        for (int i = 0; i < n; i++) {
            char curCh = fastReader.next().charAt(0);
            int cur = (int)(curCh - 'A');
            for (int k = 0; k < 2; k++) {
                char ch = fastReader.next().charAt(0);
                if (ch != '.') childs[cur][k] = (int)(ch - 'A');
                else childs[cur][k] = -1;
            }
        }
    }


    static void preOrder(int x) {
        if (x == -1) return;
        sb.append((char) (x + 'A'));
        preOrder(childs[x][0]);
        preOrder(childs[x][1]);
    }

    static void inOrder(int x) {
        if (x == -1) return;
        inOrder(childs[x][0]);
        sb.append((char) (x + 'A'));
        inOrder(childs[x][1]);
    }

    static void postOrder(int x) {
        if (x == -1) return;
        postOrder(childs[x][0]);
        postOrder(childs[x][1]);
        sb.append((char) (x + 'A'));
    }

    static void solution() {
        preOrder(0);
        sb.append("\n");
        inOrder(0);
        sb.append("\n");
        postOrder(0);
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