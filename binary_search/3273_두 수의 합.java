import java.io.*;
import java.util.*;

public class Main {
    static FastReader fastReader = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static int N, X;
    static int[] nums;

    static void input() {
        N = fastReader.nextInt();
        nums = new int[N];
        for (int index = 0; index < N; index ++) {
            nums[index] = fastReader.nextInt();
        }
        X = fastReader.nextInt();
    }

    static int binarySearch(int[] array, int target, int targetIdx, int left, int right) {
        while (left <= right) {
            int mid = (left + right) / 2;
            if (array[mid] < target) {
                left = mid + 1;
            } else if (array[mid] > target) {
                right = mid - 1;
            } else {
                if (mid == targetIdx) {
                    // 찾은 정답이 나 자신이라면 스킵
                    left = mid + 1;
                }
                return mid;
            }
        }
        return -1;
    }

    static void process() {
        // 이분 탐색을 위한 정렬
        Arrays.sort(nums);

        int ans = 0;
        for (int index = 0; index < N; index++) {
            int res = binarySearch(nums, X - nums[index], index, 0, N - 1);
            if (res >= 0) {
                ans++;
            }
        }

        // 정답 출력 (쌍의 개수를 출력하는 것이므로 2로 나눈다.)
        System.out.println(ans / 2);
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
