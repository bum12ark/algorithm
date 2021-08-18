import java.io.*;
import java.util.*;

public class Main {
    static FastReader fastReader = new FastReader();
    static StringBuilder sb = new StringBuilder();
    
    static void input() {
        N = fastReader.nextInt();
        M = fastReader.nextInt();
        selected = new int[N + 1];
        used = new boolean[N + 1];
    }

    static int N, M;
    static int[] selected;
    static boolean[] used;

    // Recurrence Function (재귀 함수)
    // 만약 M 개를 전부 고름 => 조건에 맞는 탐색 한 가지를 성공한 것!
    // 아직 M 개를 고르지 않음 => k 번째부터 M 번째 원소를 조건에 맞게 고르는 모든 방법을 시도한다.
    static void recFunc(int k) {
        if (k == M + 1) {
            // selected[1...M] 배열이 새롭게 탐색된 결과
            for (int i = 1; i <= M; i++) {
                sb.append(selected[i]).append(" ");
            }
            sb.append("\n");
        } else {
            for (int cand = 1; cand <= N; cand++) {
                boolean isUsed = false;
                for (int i = 1; i < k; i++) {
                    if (selected[i] == cand) {
                        isUsed = true;
                        break;
                    }
                }
                if (!isUsed) {
                    selected[k] = cand;
                    recFunc(k + 1);
                    selected[k] = 0;
                }
            }
        }
    }

    static void recFuncAdvanced(int k) {
        if (k == M + 1) {
            for (int i = 1; i <= M; i++) {
                sb.append(selected[i]).append(" ");
            }
            sb.append("\n");
            return;
        }
        for (int cand = 1; cand <= N; cand++) {
            if (used[cand]) continue;

            selected[k] = cand;
            used[cand] = true;

            recFuncAdvanced(k + 1);

            selected[k] = 0;
            used[cand] = false;
        }
    }

    public static void main(String[] args) {
        input();

        recFuncAdvanced(1);
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
