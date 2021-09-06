import java.io.*;
import java.util.*;

/**
 * link: https://www.acmicpc.net/problem/2003
 *
 * 2003 - 수들의 합 2
 */
public class Main {
    static FastReader fastReader = new FastReader();

    static void input() {
        N = fastReader.nextInt();
        M = fastReader.nextInt();
        nums = new int[N];
        for (int i = 0; i < N; i++) nums[i] = fastReader.nextInt();
    }

    static int N, M;
    static int[] nums;

    static int pro() {
        int right = -1, sum = 0, ans = 0;
        for (int left = 0; left < N; left++) {
            // right 를 옮길 수 있을 때 까지 옮기기
            while (right < N - 1 && sum < M) {
                sum += nums[++right];
            }

            // [left ... right] 의 합, 즉 sum 이 조건을 만족하면 정답 갱신하기
            if (sum == M) {
                ans++;
            }

            // left 을 구간에서 제외하기
            sum -= nums[left];
        }
        return ans;
    }

    public static void main(String[] args) {
        input();
        int answer = pro();
        System.out.println(answer);
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