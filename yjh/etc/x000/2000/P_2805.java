import java.util.Scanner;

public class P_2805 {
    static int N, M;
    static int[] tree;

    static boolean check(int H) {
        long sum = 0;
        for (int i = 1; i <= N; i++) {
            if (tree[i] > H)
                sum += tree[i] - H;
        }
        return sum >= M;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();
        tree = new int[N + 1];
        for (int i = 1; i <= N; i++)
            tree[i] = sc.nextInt();

        int L = 1;
        int R = 2000000000, answer = 0;
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