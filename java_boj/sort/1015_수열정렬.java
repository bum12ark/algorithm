import java.io.*;
import java.util.*;

public class Main {
    static FastReader fastReader = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static class Elem implements Comparable<Elem> {
        int num;
        int index;

        public Elem(int num, int index) {
            this.num = num;
            this.index = index;
        }

        @Override
        public int compareTo(Elem others) {
            if (num != others.num) {
                return num - others.num;
            }
            return index - others.index;
        }
    }

    static int N;
    static Elem[] B;
    static int[] P;

    static void input() {
        N = fastReader.nextInt();
        B = new Elem[N];
        P = new int[N];
        for (int index = 0; index < N; index++) {
            int value = fastReader.nextInt();
            B[index] = new Elem(value, index);
        }
    }

    static void process() {
        // TODO: B 배열 정렬하기
        Arrays.sort(B);

        // TODO: B 배열의 값을 이용해서 P 배열 채우기
        for (int bIndex = 0; bIndex < N; bIndex++) {
            P[B[bIndex].index] = bIndex;
        }

        // TODO: P 배열 출력하기기
        for (int i = 0; i < N; i++) {
            sb.append(P[i]).append(" ");
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
