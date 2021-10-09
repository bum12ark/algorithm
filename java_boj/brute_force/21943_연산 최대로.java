
import java.io.*;
import java.util.*;

/**
 * link: https://www.acmicpc.net/problem/21943
 *
 * 21943_연산 최대로
 *
 * 1. 모든 숫자의 순열의 구하기 위하여 재귀 탐색
 * 2. 순열 하나를 구하였을 경우 곱하기를 기준으로 분할하여 최대값 추출
 */
public class Main {
    static FastReader fastReader = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static int N, P, Q; // 입력될 양의 정수의 개수, 더하기 개수, 곱하기 개수
    static int[] nums, selectedSums, selectedNums;
    static boolean[] visited;
    static int ans = Integer.MIN_VALUE;

    static void input() {
        N = fastReader.nextInt();
        nums = new int[N];
        selectedNums = new int[N];
        visited = new boolean[N];

        for (int i = 0; i < N; i++) {
            nums[i] = fastReader.nextInt();
        }
        P = fastReader.nextInt();
        Q = fastReader.nextInt();
        selectedSums = new int[Q + 1];
    }

    // 중복 없이 순열 구하기
    static void permutation(int selectedCnt) {
        if (selectedCnt >= N) {
            operationDfs(selectedNums, 0, 0);
            return;
        }

        for (int i = 0; i < N; i++) {
            if (visited[i]) continue;

            visited[i] = true;
            selectedNums[selectedCnt] = nums[i];
            permutation(selectedCnt + 1);
            selectedNums[selectedCnt] = 0;
            visited[i] = false;
        }
    }

    // 중복 없이 조합 구하기
    static void operationDfs(int[] selectedNums, int index, int multiCount) {
        if (multiCount > Q) {
            if (index >= N) { // 마지막 숫자까지 조합 탐색이 완료 되었을 경우
                int sum = selectedSums[0];
                for (int i = 1; i < selectedSums.length; i++) {
                    sum *= selectedSums[i];
                }
                ans = Math.max(ans, sum);
            }
            return;
        }

        if (index >= N) return;

        // 곱하기를 선택하는 경우
        selectedSums[multiCount] += selectedNums[index];
        operationDfs(selectedNums, index + 1, multiCount + 1);

        // 곱하기를 선택하지 않는 경우
        operationDfs(selectedNums, index + 1, multiCount);
        // 여태까지 더한 값을 사용하기 위하여 여기에 위치, 위에 위치할 경우 한 개씩만 선택 된다.
        selectedSums[multiCount] -= selectedNums[index];
    }

    static void process() {
        permutation(0);
        System.out.println(ans);
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