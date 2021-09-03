import java.io.*;
import java.util.*;

/**
 * link: https://www.acmicpc.net/problem/1806
 * 
 * 1806 - 부분합
 */
public class Main {
    static FastReader fastReader = new FastReader();

    static void input() {
        N = fastReader.nextInt();
        S = fastReader.nextInt();
        nums = new int[N];
        for (int i = 0; i < N; i++) nums[i] = fastReader.nextInt();
    }

    static int N, S;
    static int[] nums;

    static int pro() {
        int right = -1, ans = N + 1, sum = 0;
        for (int left = 0; left < N; left++) {

            // right 포인터를 옮길 수 있을 때 까지 옮기기
            while (right < N - 1 && sum < S) {
                right++;
                sum += nums[right];
            }

            // [left ... right] 의 합, 즉 sum 이 조건을 만족하면 정답 갱신하기
            if (sum >= S) {
                ans = Math.min(ans, right - left + 1);
            }

            // left 포인터 증가에 따른 sum 값 갱신 (left 을 구간에서 제외)
            sum -= nums[left];
        }
        // ans 값을 보고 불가능 판단하기
        return ans == N + 1 ? 0 : ans;
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
