package com.company.boj;

import java.io.*;
import java.util.*;

/**
 * link: https://www.acmicpc.net/problem/12919
 *
 * 12919_A와 B2
 */
public class Main {
    static FastReader fastReader = new FastReader();
    static StringBuilder builder = new StringBuilder();

    static String S, T;
    static int answer;

    static void input() {
        S = fastReader.next();
        T = fastReader.next();
    }

    static void recursive(int length, String str) {
        if (length <= S.length()) {
            if (str.equals(S)) {
                answer = 1;
                return;
            }
            return;
        }

        if (str.charAt(length - 1) == 'A') {
            recursive(length - 1, str.substring(0, length - 1));
        }

        if (str.charAt(0) == 'B') {
            recursive(length - 1, new StringBuilder(str.substring(1)).reverse().toString());
        }
    }

    public static void main(String[] args) {
        input();
        recursive(T.length(), T);
        System.out.println(answer);
    }

    // FastReader
    static class FastReader {
        private BufferedReader br;
        private StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        public FastReader(String s) throws FileNotFoundException {
            br = new BufferedReader(new FileReader(new java.io.File(s)));
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
