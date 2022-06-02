import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class P_13144 {
    static int N;
    static int[] arr;
    static int[] cnt;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        cnt = new int[100001];

        long answer = 0;
        for (int L = 0, R = 0; L < N; L++) {
            while (R < N && cnt[arr[R]] == 0) {
                cnt[arr[R]] += 1;
                R += 1;
            }

            answer += R - L;

            cnt[arr[L]] -= 1;
        }

        System.out.println(answer);
    }
}
