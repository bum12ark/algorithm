import java.io.*;
import java.util.*;

public class Main {
    static FastReader fastReader = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static class MyFile implements Comparable<MyFile> {
        String name; // 이름
        String extension; // 확장자

        public MyFile(String name, String extension) {
            this.name = name;
            this.extension = extension;
        }

        @Override
        public int compareTo(MyFile others) {
            return extension.compareTo(others.extension);
        }

        @Override
        public String toString() {
            return "[" + this.name + ", " + this.extension + "]";
        }
    }

    static int N;
    static MyFile[] myFiles;

    static void input() {
        N = fastReader.nextInt();
        myFiles = new MyFile[N];
        for (int index = 0; index < N; index++) {
            String fileName = fastReader.next();
            int dotIndex = fileName.indexOf("."); // . 의 위치
            String name = fileName.substring(0, dotIndex); // 파일 이름
            String extension = fileName.substring(dotIndex + 1); // 확장자

            myFiles[index] = new MyFile(name, extension);
        }
    }

    static void process() {
        // 파일 정렬
        Arrays.sort(myFiles);

        // 파일의 개수 출력
        int currentCount = 1;
        for (int index = 1; index < N; index++) {
            String currentExtension = myFiles[index].extension;
            String prevExtension = myFiles[index - 1].extension;
            if (currentExtension.equals(prevExtension)) {
                currentCount += 1;
            } else {
                sb.append(prevExtension).append(" ").append(currentCount).append("\n");
                currentCount = 1;
            }
        }
        sb.append(myFiles[N - 1].extension).append(" ").append(currentCount);

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
