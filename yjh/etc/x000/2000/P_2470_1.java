import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class P_2470_1 {
    static int N;
    static int[] arr;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        Arrays.sort(arr);

        int L = 0, R = N - 1, v1 = 0, v2 = 0, best = Integer.MAX_VALUE;
        while (L < R) {
            int sum = arr[L] + arr[R];
            if (Math.abs(sum) < best) {
                best = Math.abs(sum);
                v1 = arr[L];
                v2 = arr[R];

                if (best == 0)
                    break;
            }

            if (sum > 0) {
                R -= 1;
            } else {
                L += 1;
            }
        }

        System.out.println(v1 + " " + v2);
    }
}
