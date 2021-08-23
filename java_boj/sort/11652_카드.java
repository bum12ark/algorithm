import java.io.*;
import java.util.*;

public class Main {
    static FastReader fastReader = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static int N;
    static long[] nums;

    static void input() {
        N = fastReader.nextInt();
        nums = new long[N];
        for (int i = 0; i < N; i++) {
            nums[i] = fastReader.nextLong();
        }
    }

    static void process() {
        Arrays.sort(nums);

        int currentCount = 1, modeCount = 1;
        long mode = nums[0];
        // 2번 원소부터 차례대로 보면서, 같은 숫자가 이어서 나오고 있는 지, 새로운 숫자가 나왔는 지를 판단하여
        // currentCount 값을 갱신해주고, 최빈값을 갱신하는 작업
        for (int index = 1; index < N; index++) {
            if (nums[index - 1] == nums[index]) {
                currentCount += 1;
            } else {
                currentCount = 1;
            }
            if (currentCount > modeCount) {
                mode = nums[index];
                modeCount = currentCount;
            }
        }

        System.out.println(mode);
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
