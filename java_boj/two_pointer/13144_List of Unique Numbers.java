import java.io.*;
import java.util.*;

/**
 * link: https://www.acmicpc.net/problem/13144
 *
 * 13144 - List of Unique Numbers
 */
public class Main {
    static FastReader fastReader = new FastReader();

    static int N;
    static int[] A, cnt;

    static void input() {
        N = fastReader.nextInt();
        A = new int[N + 1];
        for (int a = 1; a <= N; a++) A[a] = fastReader.nextInt();
        cnt = new int[N + 1];
    }

    static void pro() {
        long ans = 0;
        for (int left = 1, right = 0; left <= N; left++) {
            // R 을 옮길 수 있는 만큼 옮긴다.
            while (right + 1 <= N && cnt[A[right + 1]] < 1) {
                right += 1;
                cnt[A[right]] += 1;
            }

            // 정답을 갱신한다.
            ans += right - left + 1;

            // L 을 옮겨주면서 A[L] 의 개수를 감소시킨다.
            cnt[A[left]] -= 1;
        }
        System.out.println(ans);
    }

    public static void main(String[] args) {
        input();
        pro();
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
