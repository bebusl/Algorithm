import java.util.*;
import java.io.*;

public class P_9095 {
    static BufferedReader br;
    static StringBuffer sb;
    static int T, input;
    static int[] dp;

    public static void main(String[] args) throws Exception {
        br = new BufferedReader(new InputStreamReader(System.in));
        T = Integer.parseInt(br.readLine());

        dp = new int[11];

        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 4;

        for (int i = 4; i < 11; i++) {
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
        }

        sb = new StringBuffer();
        for (int i = 0; i < T; i++) {
            input = Integer.parseInt(br.readLine());
            sb.append(dp[input]).append("\n");
        }
        System.out.println(sb);
    }
}
