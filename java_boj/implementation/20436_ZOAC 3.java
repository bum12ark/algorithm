import java.io.*;
import java.util.*;

/**
 * link: https://www.acmicpc.net/problem/20436
 */
public class Main {
    static FastReader fastReader = new FastReader();

    static Map<Character, Pos> leftKeyboard = new HashMap<>();
    static Map<Character, Pos> rightKeyboard = new HashMap<>();
    static char leftFinger, rightFinger;
    static String keyword;

    static class Pos {
        int row, column;

        public Pos(int row, int column) {
            this.row = row;
            this.column = column;
        }
    }

    static void init() {
        leftKeyboard.put('q', new Pos(0, 0));
        leftKeyboard.put('w', new Pos(0, 1));
        leftKeyboard.put('e', new Pos(0, 2));
        leftKeyboard.put('r', new Pos(0, 3));
        leftKeyboard.put('t', new Pos(0, 4));
        leftKeyboard.put('a', new Pos(1, 0));
        leftKeyboard.put('s', new Pos(1, 1));
        leftKeyboard.put('d', new Pos(1, 2));
        leftKeyboard.put('f', new Pos(1, 3));
        leftKeyboard.put('g', new Pos(1, 4));
        leftKeyboard.put('z', new Pos(2, 0));
        leftKeyboard.put('x', new Pos(2, 1));
        leftKeyboard.put('c', new Pos(2, 2));
        leftKeyboard.put('v', new Pos(2, 3));

        rightKeyboard.put('y', new Pos(0, 5));
        rightKeyboard.put('u', new Pos(0, 6));
        rightKeyboard.put('i', new Pos(0, 7));
        rightKeyboard.put('o', new Pos(0, 8));
        rightKeyboard.put('p', new Pos(0, 9));
        rightKeyboard.put('h', new Pos(1, 5));
        rightKeyboard.put('j', new Pos(1, 6));
        rightKeyboard.put('k', new Pos(1, 7));
        rightKeyboard.put('l', new Pos(1, 8));
        rightKeyboard.put('b', new Pos(2, 4));
        rightKeyboard.put('n', new Pos(2, 5));
        rightKeyboard.put('m', new Pos(2, 6));
    }

    static void input() {
        char[] chars = fastReader.nextLine().toCharArray();

        leftFinger = chars[0];
        rightFinger = chars[2];

        keyword = fastReader.next();
    }

    static int process() {
        char[] alphabets = keyword.toCharArray();

        int count = 0;
        Pos prevLeft = leftKeyboard.get(leftFinger);
        Pos prevRight = rightKeyboard.get(rightFinger);
        for (char alphabet : alphabets) {
            if (leftKeyboard.containsKey(alphabet)) {
                Pos current = leftKeyboard.get(alphabet);
                count += calculate(prevLeft, current) + 1;
                prevLeft = current;
            } else {
                Pos current = rightKeyboard.get(alphabet);
                count += calculate(prevRight, current) + 1;
                prevRight = current;
            }
        }

        return count;
    }

    static int calculate(Pos pos1, Pos pos2) {
        return Math.abs(pos1.row - pos2.row) + Math.abs(pos1.column - pos2.column);
    }

    public static void main(String[] args) {
        init();
        input();
        int count = process();
        System.out.println(count);
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
