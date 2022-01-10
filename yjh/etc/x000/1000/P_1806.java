import java.util.Scanner;

public class P_1806 {
    static int N, S;
    static int[] arr;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        S = sc.nextInt();
        arr = new int[N + 1];
        for (int i = 1; i <= N; i++)
            arr[i] = sc.nextInt();

        int R = 1, sum = 0, answer = 0;
        for (int L = 1; L <= N; L++) {

            while (sum < S && R < N) {
                sum += arr[R];
                R += 1;
            }

            if (sum >= S) {
                if (answer == 0)
                    answer = R - L;
                else
                    answer = Math.min(answer, R - L);
            }

            sum -= arr[L];
        }

        System.out.println(answer);
    }
}
