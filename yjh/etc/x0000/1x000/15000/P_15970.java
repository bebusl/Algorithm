import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class P_15970 {

    static int N;
    static ArrayList<Integer>[] arr;

    static int getLeft(int color, int idx) {
        if (idx == 0)
            return Integer.MAX_VALUE;
        return arr[color].get(idx) - arr[color].get(idx - 1);
    }

    static int getRight(int color, int idx) {
        if (idx == arr[color].size() - 1)
            return Integer.MAX_VALUE;
        return arr[color].get(idx + 1) - arr[color].get(idx);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        arr = new ArrayList[N + 1];
        for (int color = 1; color <= N; color++) {
            arr[color] = new ArrayList<Integer>();
        }
        for (int i = 0; i < N; i++) {
            int coord = sc.nextInt();
            int color = sc.nextInt();
            arr[color].add(coord);
        }
        for (int color = 1; color <= N; color++) {
            Collections.sort(arr[color]);
        }

        int total = 0;
        for (int color = 1; color <= N; color++) {
            for (int idx = 0; idx < arr[color].size(); idx++) {
                int left = getLeft(color, idx);
                int right = getRight(color, idx);
                total += Math.min(left, right);
            }
        }

        System.out.println(total);
    }
}