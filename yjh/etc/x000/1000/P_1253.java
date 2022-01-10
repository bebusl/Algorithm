import java.io.*;
import java.util.*;

public class P_1253 {
    static int N;
    static int[] arr;

    static boolean check(int i) {
        int L = 0, R = N - 1;
        int target = arr[i];
        while (L < R) {
            if (L == i)
                L++;
            else if (R == i)
                R--;
            else {
                int sum = arr[L] + arr[R];
                if (sum < target) {
                    L++;
                } else if (sum > target) {
                    R--;
                } else {
                    return true;
                }
            }
        }

        return false;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        Arrays.sort(arr);

        int answer = 0;
        for (int i = 0; i < N; i++) {
            if (check(i))
                answer += 1;
        }

        System.out.println(answer);
    }
}
