
import java.io.*;
import java.util.*;

/**
 * link: https://www.acmicpc.net/problem/21944
 *
 * 21944_문제 추천 시스템 Version2
 */
public class Main {
    static FastReader fastReader = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static class Problem implements Comparable<Problem> {
        int number, difficulty, category;

        public Problem(int number, int difficulty) {
            this.number = number;
            this.difficulty = difficulty;
        }

        public Problem(int number, int difficulty, int category) {
            this.number = number;
            this.difficulty = difficulty;
            this.category = category;
        }

        @Override
        public int compareTo(Problem o) {
            if (difficulty != o.difficulty) return Integer.compare(difficulty, o.difficulty);
            return Integer.compare(number, o.number);
        }
    }

    static int N, M; // 문제의 개수, 명령문의 개수
    static Map<Integer, Problem> problemInfos = new HashMap<>();
    static Map<Integer, TreeSet<Problem>> categoryGroupProblems = new HashMap<>();
    static TreeSet<Problem> problems = new TreeSet<>();

    static void input() {
        N = fastReader.nextInt();

        for (int category = 0; category <= 100; category++) {
            categoryGroupProblems.put(category, new TreeSet<>());
        }

        for (int i = 0; i < N; i++) {
            int number = fastReader.nextInt();
            int difficulty = fastReader.nextInt();
            int category = fastReader.nextInt();

            // 문제 리스트에 등록
            Problem problem = new Problem(number, difficulty, category);
            problemInfos.put(number, problem);
            categoryGroupProblems.get(category).add(problem);
            problems.add(problem);
        }
        M = fastReader.nextInt();
    }

    static int getRecommendByCategory(int category, int x) {
        TreeSet<Problem> categoryProblems = categoryGroupProblems.get(category);
        if (x == 1) {
            return categoryProblems.last().number;
        }
        if (x == -1) {
            return categoryProblems.first().number;
        }
        return -1;
    }

    static int getRecommendAll(int x) {
        if (x == 1) {
            return problems.last().number;
        }
        if (x == -1) {
            return problems.first().number;
        }
        return -1;
    }

    static int getRecommendByDifficulty(int x, int difficulty) {
        // 문제 변호 비교를 위해여 -1로 세팅
        Problem compareProblem = new Problem(-1, difficulty);
        if (x == 1) {
            Problem higher = problems.higher(compareProblem);
            return higher == null ? -1 : higher.number;
        }
        if (x == -1) {
            Problem lower = problems.lower(compareProblem);
            return lower == null ? -1 : lower.number;
        }
        return -1;
    }

    static void addProblem(Problem problem) {
        problems.add(problem);
        problemInfos.put(problem.number, problem);
        categoryGroupProblems.get(problem.category).add(problem);
    }

    static void removeProblemByNumber(int number) {
        Problem removeProblem = problemInfos.get(number);

        problems.remove(removeProblem);
        categoryGroupProblems.get(removeProblem.category).remove(removeProblem);
        problemInfos.remove(removeProblem);
    }

    static void process() {

        while (M-- > 0) {
            String commend = fastReader.next();

            if ("recommend".equals(commend)) {
                int category = fastReader.nextInt();
                int x = fastReader.nextInt();

                int recommendByCategory = getRecommendByCategory(category, x);
                sb.append(recommendByCategory).append("\n");
            }
            else if ("recommend2".equals(commend)) {
                int x = fastReader.nextInt();

                int recommendAll = getRecommendAll(x);
                sb.append(recommendAll).append("\n");
            }
            else if ("recommend3".equals(commend)) {
                int x = fastReader.nextInt();
                int difficulty = fastReader.nextInt();

                int recommendByDifficulty = getRecommendByDifficulty(x, difficulty);
                sb.append(recommendByDifficulty).append("\n");
            }
            else if ("add".equals(commend)) {
                int number = fastReader.nextInt();
                int difficulty = fastReader.nextInt();
                int category = fastReader.nextInt();

                Problem problem = new Problem(number, difficulty, category);
                addProblem(problem);
            }
            else if ("solved".equals(commend)) {
                int number = fastReader.nextInt();

                removeProblemByNumber(number);
            }
        }

    }

    public static void main(String[] args) {
        input();
        process();
        System.out.println(sb.toString());
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
