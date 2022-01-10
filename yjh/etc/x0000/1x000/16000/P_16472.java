import java.io.*;
import java.util.*;

public class P_16472 {
    static int N;
    static char[] arr;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        arr = br.readLine().toCharArray();

        int answer = 0;
        int[] cnt = new int[26];
        int kind = 0;

        for (int L = 0, R = 0; R < arr.length; R++) {
            int prev = cnt[arr[R] - 'a'];
            cnt[arr[R] - 'a'] += 1;
            if (prev == 0)
                kind += 1;

            while (kind > N) {
                int prev_ = cnt[arr[L] - 'a'];
                cnt[arr[L] - 'a'] -= 1;
                if (prev_ == 1)
                    kind -= 1;
                L += 1;
            }

            answer = Math.max(answer, R - L + 1);
        }

        System.out.println(answer);
    }
}
