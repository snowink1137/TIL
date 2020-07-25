import java.util.ArrayList;

public class Survivor {
    public static int getSurvivingIndex(int n, int k) {
        // 코드를 입력하세요.
        ArrayList<Boolean> check = new ArrayList<>();

        for (int i=0; i<n; i++) {
            check.add(true);
        }

        int idx = 0;
        for (int i=n; i>1; i--) {
            int cnt = 0;
            while (cnt < k) {
                idx++;
                idx = idx % n;
                if (check.get(idx)) {
                    cnt += 1;
                }
            }

            if (idx == 0) {
                System.out.println("20번 군사가 죽습니다.");
                check.set(idx, false);
            } else {
                System.out.println(idx + "번 군사가 죽습니다.");
                check.set(idx, false);
            }

        }

        int cnt = 0;
        while (true) {
            if (check.get(cnt)) {
                return cnt;
            }
            cnt++;
        }
    }

    public static void main(String[] args) {
        System.out.println("김신은 " + getSurvivingIndex(20, 5) + "번 자리에 서있으면 됩니다.");
    }
}