import java.io.*;
import java.util.*;

public class Main {
    static FastReader fastReader = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static int N, M;
    static int[] nums, targets;

    static void input() {
        N = fastReader.nextInt();
        targets = new int[N];
        for (int i = 0; i < N; i++) {
            targets[i] = fastReader.nextInt();
        }
        M = fastReader.nextInt();
        nums = new int[M];
        for (int i = 0; i < M; i++) {
            nums[i] = fastReader.nextInt();
        }
    }

    // 찾는 값이 없을 경우 -1을 리턴한다.
    static int binarySearch(int[] array, int target, int left, int right) {
        while (left <= right) {
            int mid = (left + right) / 2;
            if (array[mid] > target) {
                right = mid - 1;
            } else if (array[mid] < target) {
                left = mid + 1;
            } else {
                return 1;
            }
        }
        return 0;
    }

    static void process() {
        Arrays.sort(targets);

        for (int index = 0; index < M; index++) {
            int res = binarySearch(targets, nums[index], 0, N - 1);
            sb.append(res).append("\n");
        }

        // 정답 출력
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
