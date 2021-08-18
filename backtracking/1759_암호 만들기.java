import java.io.*;
import java.util.*;

public class Main {
    static FastReader fastReader = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static int L, C;
    static int vowels, consonants;
    static char[] candidates, selected;

    static void input() {
        L = fastReader.nextInt();
        C = fastReader.nextInt();

        candidates = new char[C];
        selected = new char[L];
        for (int i = 0; i < C; i++) {
            candidates[i] = fastReader.next().charAt(0);
        }
    }

    static boolean isVowels(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }

    static void recFunc(int depth, int start) {
        if (depth == L && vowels >= 1 && consonants >= 2) {
            sb.append(new String(selected)).append("\n");
            return;
        }

        for (int index = start; index < C; index++) {
            if (isVowels(candidates[index])) vowels += 1;
            else consonants += 1;

            selected[depth] = candidates[index];
            recFunc(depth + 1, index + 1);
            selected[depth] = '\u0000';

            if (isVowels(candidates[index])) vowels -= 1;
            else consonants -= 1;
        }
    }

    static void process() {
        // 사전순으로 증가하는 순서로 배열되어 있기 때문에 오름차순 정렬
        Arrays.sort(candidates);
        // 재귀 함수 호출
        recFunc(0, 0);
        // 정답 호출
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
