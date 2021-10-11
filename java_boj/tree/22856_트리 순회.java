
import java.io.*;
import java.util.*;

/**
 * link: https://www.acmicpc.net/problem/22856
 *
 * 22856_트리 순회
 */
public class Main {
    static FastReader fastReader = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static class Node {
        int left, right;

        public Node(int left, int right) {
            this.left = left;
            this.right = right;
        }

        @Override
        public String toString() {
            return "Node{" +
                    "left=" + left +
                    ", right=" + right +
                    '}';
        }
    }

    static int N, answer; // 노드의 개수, 답
    static Node[] trees;

    static void input() {
        N = fastReader.nextInt();
        trees = new Node[N + 1];
        for (int i = 0; i < N; i++) {
            int nodeIndex = fastReader.nextInt();
            int left = fastReader.nextInt();
            int right = fastReader.nextInt();

            trees[nodeIndex] = new Node(left, right);
        }
    }

    static int dfsInorderEnd(int nodeIndex, int depth) {
        if (nodeIndex == -1) return depth;
        return dfsInorderEnd(trees[nodeIndex].right, depth + 1);
    }

    static void process() {
        answer = 2 * (N - 1);
        int rootToInorderEnd = dfsInorderEnd(1, 0);
        answer -= (rootToInorderEnd - 1);

        System.out.println(answer);
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
/*
6
1 2 3
2 -1 -1
3 4 -1
4 5 6
5 -1 -1
6 -1 -1
 */
