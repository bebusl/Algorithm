import java.util.*;
import java.io.*;

public class P_11057 {
    static BufferedReader br;
    static int N;
    static int[][] dp;

    public static void main(String[] args) throws Exception {
        br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        dp = new int[N + 1][10];

        for (int i = 0; i < 10; i++)
            dp[1][i] = 1;

        for (int i = 2; i <= N; i++) {
            for (int j = 0; j < 10; j++) {
                for (int plus = 0; plus <= j; plus++) {
                    dp[i][j] += dp[i - 1][plus];
                    dp[i][j] %= 10007;
                }
            }
        }

        int answer = 0;
        for (int i = 0; i < 10; i++)
            answer += dp[N][i];

        System.out.println(answer % 10007);
    }
}
