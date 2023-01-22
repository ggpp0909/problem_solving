import java.util.Arrays;
import java.util.Scanner;

public class Main_10844 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();

        long[][] dp = new long[101][10];
        for (int i = 1; i < 10; i++) {
            dp[1][i] = 1;
        }

        for (int i = 2; i < 101; i++) {
            for (int j = 0; j < 10; j++) {
                if (j == 0) {
                    dp[i][j] = dp[i - 1][1] % 1_000_000_000L;
                } else if (j == 9) {
                    dp[i][j] = dp[i - 1][8] % 1_000_000_000L;
                } else {
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1] % 1_000_000_000L;
                }
            }
        }

        long ans = Arrays.stream(dp[num]).sum() % 1_000_000_000L;
        System.out.println(ans);
    }
}
