package com.company.boj;

import java.io.*;
import java.util.*;

/**
 * link: https://www.acmicpc.net/problem/4659
 *
 * 4659_비밀번호 발음하기
 */
public class Main {
    static FastReader fastReader = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static List<String> testCases = new ArrayList<>();
    static Set<Character> vowels = Set.of('a', 'e', 'i', 'o', 'u');

    static void input() {
        boolean flag = true;
        while (flag) {
            String testCase = fastReader.next();
            if (testCase.equals("end")) {
                flag = false;
            } else {
                testCases.add(testCase);
            }
        }
    }

    // 1. 모음 포함 여부
    static boolean isContainVowel(String word) {
        for (Character c : word.toCharArray()) {
            if (vowels.contains(c)) return true;
        }
        return false;
    }

    static boolean isVowel(Character c) {
        return vowels.contains(c);
    }

    static boolean isContinuous(String word, int count) {
        char prev = word.charAt(0);
        int continuousCount = 1;

        for (int i = 1; i < word.length(); i++) {
            char current = word.charAt(i);

            if ((isVowel(prev) && isVowel(current))
                    || !isVowel(prev) && !isVowel(current)) {
                continuousCount += 1;
            } else {
                continuousCount = 1;
            }

            if (continuousCount >= count) return true;

            prev = current;
        }

        return false;
    }

    static boolean isSameWord(String word) {
        char prev = word.charAt(0);
        int count = 1;

        for (int i = 1; i < word.length(); i++) {
            char current = word.charAt(i);
            if (prev == current) count += 1;
            else count = 1 ;

            if (count >= 2) {
                if (current == 'e' || current == 'o') continue;
                return true;
            }
            prev = current;
        }

        return false;
    }

    static boolean validate(String word) {

        if (!isContainVowel(word)) return false;
        if (isContinuous(word, 3)) return false;
        if (isSameWord(word)) return false;

        return true;
    }

    public static void main(String[] args) {
        input();
        for (String testCase : testCases) {
            if (validate(testCase)) {
                sb.append("<").append(testCase).append("> is acceptable.\n");
            } else {
                sb.append("<").append(testCase).append("> is not acceptable.\n");
            }
        }
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
