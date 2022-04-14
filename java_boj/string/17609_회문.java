import java.io.*;
import java.util.*;

/**
 * link: https://www.acmicpc.net/problem/17609
 *
 * 17609_회문
 */
public class Main {
    static FastReader fastReader = new FastReader();

    static int T;

    static int process(String str) {
        if (isPalindrome(str, 0, str.length() - 1)) return 0;
        if (isPseudo(str)) return 1;
        return 2;
    }

    static boolean isPalindrome(String str, int left, int right) {
        while (left <= right) {
            if (str.charAt(left) == str.charAt(right)) {
                left += 1;
                right -= 1;
            } else {
                return false;
            }
        }
        return true;
    }

    static boolean isPseudo(String str) {
        int left = 0, right = str.length() - 1;
        while (left <= right) {
            if (str.charAt(left) != str.charAt(right)) {
                if (isPalindrome(str, left + 1, right)) return true;
                return isPalindrome(str, left, right - 1);
            }
            left += 1;
            right -= 1;
        }
        return true;
    }

    public static void main(String[] args) {
        T = fastReader.nextInt();
        while (T-- > 0) {
            int answer = process(fastReader.next());
            System.out.println(answer);
        }
    }

    // FastReader
    static class FastReader {
        private BufferedReader br;
        private StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        public FastReader(String s) throws FileNotFoundException {
            br = new BufferedReader(new FileReader(new java.io.File(s)));
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
