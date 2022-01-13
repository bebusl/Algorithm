import java.util.*;
import java.io.*;

public class P_2579 {
    static BufferedReader br;
    static int N;
    static int[] arr, dp;

    public static void main(String[] args) throws Exception {
        br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        arr = new int[N + 1];
        for (int i = 1; i <= N; i++)
            arr[i] = Integer.parseInt(br.readLine());

        dp = new int[301];

        dp[1] = arr[1];
        dp[2] = arr[1] + arr[2];
        for (int i = 3; i <= N; i++) {
            dp[i] = Math.max(dp[i - 3] + arr[i - 1] + arr[i], dp[i - 2] + arr[i]);
        }

        System.out.println(dp[N]);
    }
}
