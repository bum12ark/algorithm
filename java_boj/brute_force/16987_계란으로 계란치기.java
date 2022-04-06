import java.io.*;
import java.util.*;

/**
 * link: https://www.acmicpc.net/problem/16987
 *
 * 16987_계란으로 계란치기
 */
public class Main {
    static FastReader fastReader = new FastReader();

    static int N; // 계란의 수 (1 <= N <= 8)
    static List<Egg> eggs = new ArrayList<>();
    static int answer = Integer.MIN_VALUE;

    static class Egg {
        int durability;
        int weight;

        public Egg(int durability, int weight) {
            this.durability = durability;
            this.weight = weight;
        }

    }

    static void input() {
        N = fastReader.nextInt();
        while (N-- > 0) {
            int durability = fastReader.nextInt();
            int weight = fastReader.nextInt();
            eggs.add(new Egg(durability, weight));
        }
    }

    static void recursive(int index) {
        if (index == eggs.size()) {
            int count = 0;
            for (Egg egg : eggs) {
                if (egg.durability <= 0) count += 1;
            }
            answer = Math.max(answer, count);
            return;
        }

        // 손에 쥔 계란이 깨진 경우
        Egg egg = eggs.get(index);
        if (egg.durability <= 0) {
            recursive(index + 1);
        } else {
            boolean tryBroke = false;
            for (int i = 0; i < eggs.size(); i++) {
                Egg compareEgg = eggs.get(i);

                if (index == i) continue;
                if (compareEgg.durability <= 0) continue; // 다른 계란이 깨졌을 경우

                // 계란을 깨는 경우
                tryBroke = true;
                egg.durability -= compareEgg.weight;
                compareEgg.durability -= egg.weight;

                recursive(index + 1);

                egg.durability += compareEgg.weight;
                compareEgg.durability += egg.weight;
            }
            // 한번도 깬것이 없다면 다음 계란 호출
            if (!tryBroke) recursive(index + 1);
        }

    }

    public static void main(String[] args) {
        input();
        recursive(0);
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
