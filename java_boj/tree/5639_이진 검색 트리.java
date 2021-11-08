

import java.io.*;
import java.util.*;

/**
 * link: https://www.acmicpc.net/problem/5639
 *
 * 5639_이진 검색 트리
 *
 */
public class Main {
    static FastReader fastReader = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static class TreeNode {
        int node;
        TreeNode left;
        TreeNode right;

        public TreeNode(int node) {
            this.node = node;
        }

        public void insert(int n) {
            if (n < this.node) {
                if (left == null) {
                    this.left = new TreeNode(n);
                } else {
                    this.left.insert(n);
                }
            } else {
                if (right == null) {
                    this.right = new TreeNode(n);
                } else {
                    this.right.insert(n);
                }
            }
        }

        @Override
        public String toString() {
            return "[" + node + ", " + left + ", " + right + "]";
        }
    }

    static TreeNode root;

    static void input() {
        root = new TreeNode(fastReader.nextInt());

        while (true) {
            String n = fastReader.nextLine();
            if (n == null || n.equals("")) break;
            root.insert(Integer.parseInt(n));
        }
    }

    static void postOrder(TreeNode treeNode) {
        if (treeNode == null) return;
        postOrder(treeNode.left);
        postOrder(treeNode.right);
        System.out.println(treeNode.node);
    }

    static void solution() {
        postOrder(root);
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