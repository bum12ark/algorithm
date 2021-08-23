import java.io.*;
import java.util.*;

/**
 * 21608 - 상어 초등학교
 *
 * 1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
 * 2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
 * 3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로,
 *    그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
 */
public class Main {
    static FastReader fastReader = new FastReader();

    static class Seat implements Comparable<Seat> {
        int x, y, likeCnt, emptyCnt; // x 좌표, y 좌표, 좋아하는 학생이 인접한 칸, 비어있는 인접한 칸

        public Seat(int x, int y, int likeCnt, int emptyCnt) {
            this.x = x;
            this.y = y;
            this.likeCnt = likeCnt;
            this.emptyCnt = emptyCnt;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Seat seat = (Seat) o;
            return x == seat.x && y == seat.y;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }

        @Override
        public int compareTo(Seat o) {
            if (likeCnt != o.likeCnt) return Integer.compare(o.likeCnt, likeCnt);
            if (emptyCnt != o.emptyCnt) return Integer.compare(o.emptyCnt, emptyCnt);
            if (x != o.x) return Integer.compare(x, o.x);
            return Integer.compare(y, o.y);
        }

    }

    static class Pos {
        int x, y;

        public Pos(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static int N;
    static int[][] seats; // 어느자리에 누가 앉았는지를 기록하는 배열
    static Map<Integer, Pos> posMap = new HashMap<>(); // key: 학생 번호, value: 앉은 좌표
    static Map<Integer, int[]> personWhoLike = new HashMap<>();
    static int[][] dir = new int[][] {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    static void input() {
        N = fastReader.nextInt();

        seats = new int[N + 1][N + 1];
        for (int i = 0; i <= N; i++) {
            for (int j = 0; j <= N; j++) {
                seats[i][j] = -1;
            }
        }
    }

    // seat[x][y] 좌표의 인접 빈자리의 개수를 리턴하는 함수
    static int calEmptySeatCount(int x, int y) {
        int res = 0;
        for (int i = 0; i < 4; i++) {
            int nextX = x + dir[i][0];
            int nextY = y + dir[i][1];

            if (nextX < 1 || nextY < 1 || nextX > N || nextY > N) continue;
            if (seats[nextX][nextY] == -1) res += 1;
        }
        return res;
    }

    // seat[x][y] 좌표의 인접 좋아하는 사람이 앉은 개수
    static int calLikePersonCount(int x, int y, int[] likes) {
        int res = 0;
        for (int i = 0; i < 4; i++) {
            int nextX = x + dir[i][0];
            int nextY = y + dir[i][1];

            if (nextX < 1 || nextY < 1 || nextX > N || nextY > N) continue;
            if (seats[nextX][nextY] == -1) continue;
            boolean isLikeSeat = Arrays.stream(likes).anyMatch(value -> value == seats[nextX][nextY]);
            if (isLikeSeat) res++;
        }
        return res;
    }

    // 학생을 자리에 앉히는 함수
    static void takeSeat(int number, int x, int y) {
        seats[x][y] = number;
        posMap.put(number, new Pos(x, y));
    }

    // 가능한 인접 List 를 리턴하는 함수
    static List<Seat> getAvailableSeats(int x, int y, int[] likes) {
        List<Seat> res = new ArrayList<>();
        for (int i = 0; i < 4; i++) {
            int nextX = x + dir[i][0];
            int nextY = y + dir[i][1];

            if (nextX < 1 || nextY < 1 || nextX > N || nextY > N) continue;
            if (seats[nextX][nextY] != -1) continue;

            int likeCnt = calLikePersonCount(nextX, nextY, likes);
            int emptyCnt = calEmptySeatCount(nextX, nextY);
            res.add(new Seat(nextX, nextY, likeCnt, emptyCnt));
        }
        return res;
    }

    // 조건에 맞게 자리를 배정정
   static void setFriendSeat(int number, int[] likes) {
        TreeSet<Seat> seatTreeSet = new TreeSet<>();
        for (int friend : likes) {
            if (posMap.containsKey(friend)) {
                Pos friendPos = posMap.get(friend);
                List<Seat> available = getAvailableSeats(friendPos.x, friendPos.y, likes);
                seatTreeSet.addAll(available);
            }
        }

        if (seatTreeSet.isEmpty()) {
            for (int i = 1; i <= N; i++) {
                for (int j = 1; j <= N; j++) {
                    if (seats[i][j] == -1) {
                        seatTreeSet.add(new Seat(i, j, calLikePersonCount(i, j, likes), calEmptySeatCount(i, j)));
                    }
                }
            }
            Seat priority = seatTreeSet.first();
            takeSeat(number, priority.x, priority.y);
            return;
        }

        Seat priority = seatTreeSet.first();
        takeSeat(number, priority.x, priority.y);
    }

    static void process() {
        int cnt = N * N;
        while (cnt-- > 0) {
            int[] likes = new int[4];
            int number = fastReader.nextInt();
            for (int i = 0; i < 4; i++) {
                likes[i] = fastReader.nextInt();
            }

            personWhoLike.put(number, likes);
            // 탐색 시작
            setFriendSeat(number, likes);
        }

        int ans = calculateAnswer();
        System.out.println(ans);
    }

    static int calculateAnswer() {
        int res = 0;
        for (int x = 1; x <= N; x++) {
            for (int y = 1; y <= N; y++) {
                int[] likes = personWhoLike.get(seats[x][y]);
                int satisfaction = calLikePersonCount(x, y, likes);

                if (satisfaction == 1) {
                    res += 1;
                } else if (satisfaction == 2) {
                    res += 10;
                } else if (satisfaction == 3) {
                    res += 100;
                } else if (satisfaction == 4) {
                    res += 1000;
                }
            }
        }
        return res;
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
