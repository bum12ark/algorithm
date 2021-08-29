import java.io.*;
import java.util.*;

public class Main {
    static FastReader fastReader = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static int N, M;
    static int[] nums, selected;
    static boolean[] visited;

    static void input() {
        N = fastReader.nextInt();
        M = fastReader.nextInt();

        nums = new int[N];
        for (int i = 0; i < N; i++) {
            nums[i] = fastReader.nextInt();
        }
        selected = new int[M];
        visited = new boolean[N];
    }

    static void recFunc(int depth) {
        if (depth == M) {
            for (int i = 0; i < M; i++) sb.append(selected[i]).append(" ");
            sb.append("\n");
            return;
        }

        int prevNum = 0;
        for (int index = 0; index < N; index++) {
            int num = nums[index];
            if (visited[index]) continue;
            // 정렬 되어 있는 상태이므로 이전 값과 같은 값이라면 중복된 값이다!
            if (prevNum == num) continue;
            prevNum = num;

            selected[depth] = num;
            visited[index] = true;
            recFunc(depth + 1);
            visited[index] = false;
            selected[depth] = 0;
        }
    }

    static void process() {
        // 서전순으로 증가하는 수열을 위한 오름차순 정렬
        Arrays.sort(nums);
        // 재귀 호출 시작
        recFunc(0);
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
