import java.io.*;
import java.util.*;

public class Main {
    static FastReader fastReader = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static int N;
    static Map<Integer, List<Integer>> colorMap = new HashMap<>();

    static void input() {
        N = fastReader.nextInt();

        for (int color = 1; color <= N; color ++) colorMap.put(color, new ArrayList<>());
        for (int i = 1; i <= N; i++) {
            int coordinate = fastReader.nextInt();
            int color = fastReader.nextInt();
            colorMap.get(color).add(coordinate);
        }
    }

    // 색깔이 color 인 점의 idx 번째에 있는 점이 왼쪽으로 화살표를 그린다면
    // 화살표의 길이를 return 하는 함수. 왼쪽에 점이 없다면 무한대를 return.
    static int toLeft(int index, int color) {
        if (index == 0) {
            return Integer.MAX_VALUE;
        }
        List<Integer> colorList = colorMap.get(color);
        return colorList.get(index) - colorList.get(index - 1);
    }

    // 색깔이 color 인 점의 idx 번째에 있는 점이 오른쪽으로 화살표를 그린다면
    // 화살표의 길이를 return 하는 함수. 오른쪽에 점이 없다면 무한대를 return.
    static int toRight(int index, int color) {
        List<Integer> colorList = colorMap.get(color);
        if (index == colorList.size() - 1) {
            return Integer.MAX_VALUE;
        }
        return colorList.get(index + 1) - colorList.get(index);
    }

    static void process() {
        // 색깔별로 정렬하기
        for (int color = 1; color <= N; color++) {
            Collections.sort(colorMap.get(color));
        }

        int ans = 0;
        for (int color = 1; color <= N; color++) {
            // 색깔 별로, 각 점마다 가장 가까운 점 찾아주기
            List<Integer> colorList = colorMap.get(color);
            for (int index = 0; index < colorList.size(); index++) {
                int left = toLeft(index, color); // 왼쪽 점 까지의 거리
                int right = toRight(index, color); // 오른쪽 점 까지의 거리
                ans += Math.min(left, right);
            }
        }

        // 정답 출력하기
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
