import java.util.*;
import java.io.*;

public class BOJ1931 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int timeList[][] = new int[n][2];

        for (int i = 0; i < n; i++) {
            timeList[i][0] = sc.nextInt();
            timeList[i][1] = sc.nextInt();
        }
        Arrays.sort(timeList, (a, b) -> {
            if(a[1] == b[1]) return a[0] - b[0];
            return a[1] - b[1];
        });
        int ans = 0;
        int time = 0;

        for (int i = 0; i < n; i++) {
            // 다음회의시작시각 >= 이전회의종료시각
            if (timeList[i][0] >= time) {
                time = timeList[i][1];
                ans++;
            }
        }
        System.out.println(ans);

    }
}
