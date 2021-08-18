import java.io.*;
import java.util.*;

public class Main {
    static FastReader fastReader = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static int N;
    static String[] words;

    static void input() {
        N = fastReader.nextInt();
        words = new String[N];
        for (int index = 0; index < N; index++) {
            words[index] = fastReader.next();
        }
    }

    static void process() {
        Arrays.sort(words, (o1, o2) -> {
            if (o1.length() != o2.length()) { // 길이가 짧은 순서대로 오름차순
                return Integer.compare(o1.length(), o2.length());
            }
            return o1.compareTo(o2); // 사전순으로 오름차순
        });

        // 중복되지 않은 단어만 고르기
        sb.append(words[0]).append("\n");
        for (int index = 1; index < N; index++) {
            if (!words[index].equals(words[index - 1])) {
                sb.append(words[index]).append("\n");
            }
        }

        // 정답출력
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
