
import java.io.*;
import java.util.*;

/**
 * link: https://www.acmicpc.net/problem/21939
 *
 * 21939 문제 추천 시스템 Version 1
 *
 * [TreeSet]
 * TreeSet의 remove 메소드는 equals와 hascode를 사용하여 삽입, 수정, 삭제를 하지 않는다.
 * compareTo 메소드를 사용하여 삽입, 수정, 삭제 처리를 한다.
 */
public class Main {
    static FastReader fastReader = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static class Problem implements Comparable<Problem> {
        int number, difficulty;

        public Problem(int number, int difficulty) {
            this.number = number;
            this.difficulty = difficulty;
        }

        @Override
        public int compareTo(Problem o) {
            if (difficulty != o.difficulty) {
                return Integer.compare(difficulty, o.difficulty);
            }
            return Integer.compare(number, o.number);
        }
    }

    static int N, M; // 문제의 개수, 명령문의 개수
    static TreeSet<Problem> problems = new TreeSet<>();
    static Map<Integer, Integer> difficulties = new HashMap<>();

    static void input() {
        N = fastReader.nextInt();
        for (int i = 0; i < N; i++) {
            int number = fastReader.nextInt();
            int difficulty = fastReader.nextInt();

            problems.add(new Problem(number, difficulty));
            difficulties.put(number, difficulty);
        }
        M = fastReader.nextInt();
    }

    static int getRecommendNumber(int x) {
        if (x == 1) {
            return problems.last().number;
        } else if (x == -1) {
            return problems.first().number;
        }
        return -1;
    }

    static void addRecommendProblem(int number, int difficulty) {
        problems.add(new Problem(number, difficulty));
        difficulties.put(number, difficulty);
    }

    static void removeRecommendProblem(int number) {
        Integer difficulty = difficulties.get(number);
        problems.remove(new Problem(number, difficulty));
    }

    static void process() {
        StringBuilder sb = new StringBuilder();

        while (M-- > 0) {
            String command = fastReader.next();

            if ("recommend".equals(command)) {
                int x = fastReader.nextInt();
                int recommendNumber = getRecommendNumber(x);
                sb.append(recommendNumber).append("\n");
            } else if ("add".equals(command)) {
                int number = fastReader.nextInt();
                int difficulty = fastReader.nextInt();
                addRecommendProblem(number, difficulty);
            } else if ("solved".equals(command)) {
                int number = fastReader.nextInt();
                removeRecommendProblem(number);
            }
        }

        System.out.println(sb);
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
