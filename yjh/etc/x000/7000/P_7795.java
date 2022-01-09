import java.util.Arrays;
import java.util.Scanner;

public class P_7795 {
    static int T, N, M;
    static int[] A, B;

    static int lower_bound(int[] arr, int L, int R, int value) {
        int result = L - 1;
        while (L <= R) {
            int mid = (L + R) / 2;
            if (arr[mid] < value) {
                result = mid;
                L = mid + 1;
            } else if (arr[mid] >= value) {
                R = mid - 1;
            }
        }
        return result;
    }

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            T = sc.nextInt();
            for (int t = 0; t < T; t++) {
                N = sc.nextInt();
                M = sc.nextInt();
                A = new int[N + 1];
                B = new int[M + 1];
                for (int i = 1; i <= N; i++)
                    A[i] = sc.nextInt();
                for (int i = 1; i <= M; i++)
                    B[i] = sc.nextInt();

                Arrays.sort(B);

                int total = 0;
                for (int i = 1; i <= N; i++) {
                    total += lower_bound(B, 1, M, A[i]);
                }
                System.out.println(total);
            }
        }
    }
}
