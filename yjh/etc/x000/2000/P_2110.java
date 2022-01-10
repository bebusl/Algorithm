import java.util.Arrays;
import java.util.Scanner;

public class P_2110 {
    static int N, C;
    static int[] arr;

    static boolean check(int d) {
        int count = 1;
        int last = arr[1];
        for (int i = 2; i <= N; i++) {
            if (arr[i] - last >= d) {
                count += 1;
                last = arr[i];
            }
        }
        return count >= C;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        C = sc.nextInt();
        arr = new int[N + 1];
        for (int i = 1; i <= N; i++)
            arr[i] = sc.nextInt();

        Arrays.sort(arr);

        int L = 1, R = 1000000000, answer = 0;
        while (L <= R) {
            int mid = (L + R) / 2;
            if (check(mid)) {
                answer = mid;
                L = mid + 1;
            } else {
                R = mid - 1;
            }
        }

        System.out.println(answer);
    }
}
