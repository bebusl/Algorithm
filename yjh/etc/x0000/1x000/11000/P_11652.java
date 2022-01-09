import java.util.Arrays;
import java.util.Scanner;

public class P_11652 {
    static int N;
    static long[] arr;

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            N = sc.nextInt();
            arr = new long[N];
            for (int i = 0; i < N; i++) {
                arr[i] = sc.nextLong();
            }
        }
        Arrays.sort(arr);

        long mode = arr[0];
        int modeCnt = 1, curCnt = 1;

        for (int i = 1; i < N; i++) {
            if (arr[i] != arr[i - 1]) {
                curCnt = 1;
            } else {
                curCnt += 1;
            }
            if (modeCnt < curCnt) {
                mode = arr[i];
                modeCnt = curCnt;
            }
        }

        System.out.println(mode);
    }
}