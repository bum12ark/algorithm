
import java.io.*;
import java.util.*;

/**
 * link: https://www.acmicpc.net/problem/21942
 *
 * 21942 부품 대여장
 * 
 * 2021년 부터 타임스탬프까지 총 몇분인지 계산 비교
 * Map을 사용하여 부품 대여장을 설계
 * TreeMap을 사용하여 벌금 목록을 설계 (사전순으로 출력하기 위해)
 */
public class Main {
    static FastReader fastReader = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static int N, F; // 대여장 정보 개수, 벌금 (분당)
    static String L; // 대여기간 (DDD/hh:mm)
    static long rentalPeriodMinute; // 대여기간
    static int[] monthDays = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    static Map<String, Map<String, Long>> rentalMap = new HashMap<>(); // (빌린사람이름 : (빌린물건 : 빌린시간))
    static TreeMap<String, Long> fineMap = new TreeMap<>(); // 벌금 (닉네임 : 벌금액)

    static void input() {
        N = fastReader.nextInt();
        L = fastReader.next();
        F = fastReader.nextInt();

        String[] LSplit = L.split("/");
        int day = Integer.parseInt(LSplit[0]);
        int hour = Integer.parseInt(LSplit[1].split(":")[0]);
        int minute = Integer.parseInt(LSplit[1].split(":")[1]);

        rentalPeriodMinute = (((day * 24) + hour) * 60) + minute;
    }

    // 2021-01-01 부터 몇분이 지났는 지 확인 하는 메소드
    static long getTimeToMinutes(String yearMonthDay, String hourMinute) {
        String[] yearMonthDaySplit = yearMonthDay.split("-");
        int year = Integer.parseInt(yearMonthDaySplit[0]);
        int month = Integer.parseInt(yearMonthDaySplit[1]);
        int day = Integer.parseInt(yearMonthDaySplit[2]);

        String[] hourMinuteSplit = hourMinute.split(":");
        int hour = Integer.parseInt(hourMinuteSplit[0]);
        int minute = Integer.parseInt(hourMinuteSplit[1]);

        long result = 0;

        // 월, 일을 분으로 변환
        int monthToDay = day - 1;
        for (int i = 0; i < month; i++) {
            monthToDay += monthDays[i];
        }
        long dayToMinute = monthToDay * 24 * 60;

        // 시, 분을 분으로 변환
        long hourToMinute = (hour * 60) + minute;

        result = dayToMinute + hourToMinute;
        return result;
    }

    static void process() {
        while (N-- > 0) {
            String yearMonthDay = fastReader.next();
            String hourMinute = fastReader.next();
            String product = fastReader.next();
            String nickname = fastReader.next();

            long currentMinute = getTimeToMinutes(yearMonthDay, hourMinute);
            if (rentalMap.containsKey(nickname)) { // 빌린적이 있냐
                Map<String, Long> materialMap = rentalMap.get(nickname);

                if (materialMap.containsKey(product)) { // 반납일 경우
                    long startMinute = materialMap.get(product);
                    long fineMinute = currentMinute - startMinute;

                    materialMap.remove(product);
                    if (fineMinute > rentalPeriodMinute) {
                        long fine = (fineMinute - rentalPeriodMinute) * F; // 렌탈 기간은 벌금에서 제외
                        // 벌금 갱신
                        fineMap.put(nickname, fineMap.getOrDefault(nickname, 0L) + fine);
                    }
                } else { // 대여일 경우
                    materialMap.put(product, currentMinute);
                }
            } else {
                rentalMap.put(nickname, new HashMap<>());
                rentalMap.get(nickname).put(product, currentMinute);
            }
        }

        // 벌금 사전순으로 출력
        if (!fineMap.isEmpty()) {
            for (String nickname : fineMap.keySet()) {
                sb.append(nickname).append(" ").append(fineMap.get(nickname)).append("\n");
            }
        } else {
            sb.append(-1);
        }
    }

    public static void main(String[] args) {
        input();
        process();
        System.out.println(sb);
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