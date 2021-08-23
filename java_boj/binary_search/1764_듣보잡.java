import java.io.*;
import java.util.*;

public class Main {
    static FastReader fastReader = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static int N, M;
    static String[] numsA, numsB;
    static List<String> result = new ArrayList<>();

    static void input() {
        N = fastReader.nextInt();
        M = fastReader.nextInt();
        numsA = new String[N];
        numsB = new String[M];
        for (int n = 0; n < N; n++) {
            numsA[n] = fastReader.nextLine();
        }
        for (int m = 0; m < M; m++) {
            numsB[m] = fastReader.nextLine();
        }
    }

    static int binarySearch(String[] array, String target, int left, int right) {
        while (left <= right) {
            int mid = (left + right) / 2;
            int compare = array[mid].compareTo(target);
            // 음수일 경우 사전순으로 앞에 있음
            // 즉 target 값이 mid 값 뒤에 있음
            if (compare < 0) {
                left = mid + 1;
            } else if (compare > 0) {
                right = mid - 1;
            } else {
                return mid;
            }
        }
        return -1;
    }

    static void process() {
        // 이분 탐색을 위한 정렬
        Arrays.sort(numsA);
        Arrays.sort(numsB);

        // 이분 탐색 시작
        for (int index = 0; index < M; index++) {
            int res = binarySearch(numsA, numsB[index], 0, N - 1);
            if (res >= 0) {
                result.add(numsB[index]);
            }
        }

        // 정답
        sb.append(result.size()).append("\n");
        for (String word : result) {
            sb.append(word).append("\n");
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
