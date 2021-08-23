import java.io.*;
import java.util.*;

public class Main {
    static FastReader fastReader = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static class GradeCard implements Comparable<GradeCard> { // 성적표
        String name;
        int korean, english, math;

        public GradeCard(String name, int korean, int english, int math) {
            this.name = name;
            this.korean = korean;
            this.english = english;
            this.math = math;
        }

        @Override
        public int compareTo(GradeCard others) {
            if (korean != others.korean) {
                return others.korean - korean; // 내림 차순
            }
            if (english != others.english) {
                return english - others.english; // 오름 차순
            }
            if (math != others.math) {
                return others.math - math; // 내림 차순
            }
            return name.compareTo(others.name);
        }
    }

    static int N;
    static GradeCard[] cards;

    static void input () {
        N = fastReader.nextInt();
        cards = new GradeCard[N];
        for (int i = 0; i < N; i++) {
            String name = fastReader.next();
            int korean = fastReader.nextInt();
            int english = fastReader.nextInt();
            int math = fastReader.nextInt();

            cards[i] = new GradeCard(name, korean, english, math);
        }
    }

    static void process() {
        Arrays.sort(cards);

        for (GradeCard c : cards) {
            sb.append(c.name).append("\n");
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
