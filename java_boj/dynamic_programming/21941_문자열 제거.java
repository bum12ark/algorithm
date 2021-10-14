import java.io.*;
import java.util.*;

/**
 * link: https://www.acmicpc.net/problem/21941
 *
 *
 * DP를 이용해서 풀이
 * String.indexOf(String str, int fromIndex)
 * - String 문자열의 str 문자가 fromIndex 포함하여 이후 부터 존재할 경우 첫번째 인덱스 반환
 */
public class Main {
    static FastReader fastReader = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static class Pair {
        int length, score;

        public Pair(int length, int score) {
            this.length = length;
            this.score = score;
        }
    }

    static String S;
    static int M;
    static Map<String, Integer> scores = new HashMap<>();
    // 해당 인덱스에서 시작하여 매칭되는 문자열의 길이와 점수를 기록
    static List<List<Pair>> indexPairs = new ArrayList<>();
    static int[] dp;

    static void input() {
        S = fastReader.next();
        dp = new int[S.length() + 1];
        for (int i = 0; i < S.length(); i++) {
            indexPairs.add(new ArrayList<>());
        }

        M = fastReader.nextInt();
        for (int i = 0; i < M; i++) {
            String A = fastReader.next();
            int X = fastReader.nextInt();
            scores.put(A, X);
        }
    }

    static void preprocess() {
        for (String A : scores.keySet()) {
            int score = scores.get(A);

            int index = 0;
            while (index < S.length()) { // 모든 인덱스에 대하여 매칭되는 문자열 기록
                int current = S.indexOf(A, index); // 찾는 문자열이, index 부터 존재할 경우 첫 인덱스 반환
                if (current == -1) break; // 찾는 문자열이 없을 경우
                indexPairs.get(current).add(new Pair(A.length(), score));
                index = current + 1;
            }
        }
    }

    static void process() {
        for (int i = 0; i < S.length(); i++) {
            dp[i + 1] = Math.max(dp[i + 1], dp[i] + 1); // 단순히 한 문자만 지우는 경우

            List<Pair> pairs = indexPairs.get(i);
            for (int j = 0; j < pairs.size(); j++) {
                Pair pair = pairs.get(j);
                int length = pair.length;
                int score = pair.score;
                dp[i + length] = Math.max(dp[i + length], dp[i] + score);
            }
        }
        System.out.println(dp[S.length()]);
    }

    public static void main(String[] args) {
        input();
        preprocess();
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
