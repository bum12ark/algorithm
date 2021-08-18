import java.io.*;
import java.util.*;

public class Main {
    static FastReader fastReader = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static void input() {
        N = fastReader.nextInt();
        M = fastReader.nextInt();
        A = new int[N];
        B = new int[M];
        for (int i = 0; i < N; i++) A[i] = fastReader.nextInt();
        for (int i = 0; i < M; i++) B[i] = fastReader.nextInt();
    }

    static int N, M;
    static int[] A, B;

    static int lowerBound(int[] A, int x, int lo, int hi) {
        // 없을 때의 값을 잘 설정하는 것이 중요하다.
        int result = lo - 1;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (A[mid] < x) {
                result = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return result;
    }

    static int solution() {
        // 탐색 대상 오름차순 정렬
        Arrays.sort(B);
        int answer = 0;

        for (int index = 0; index < N; index++) {
            answer += lowerBound(B, A[index], 0, M - 1) + 1;
        }

        return answer;
    }

    public static void main(String[] args) {
        int T;
        T = fastReader.nextInt();
        for (int t = 0; t < T; t++) {
            input();
            System.out.println(solution());
        }
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
