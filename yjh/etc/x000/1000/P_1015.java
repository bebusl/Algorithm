import java.util.Arrays;
import java.util.Scanner;

public class P_1015 {

    static class Elem implements Comparable<Elem> {
        public int value, idx;

        @Override
        public int compareTo(Elem o) {
            if (value != o.value)
                return value - o.value;
            return idx - o.idx;
        }
    }

    static int N;
    static Elem[] B;
    static int[] P;

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            N = sc.nextInt();
            B = new Elem[N];
            P = new int[N];
            for (int i = 0; i < N; i++) {
                B[i] = new Elem();
                B[i].value = sc.nextInt();
                B[i].idx = i;
            }
        }
        Arrays.sort(B);

        for (int b_idx = 0; b_idx < N; b_idx++) {
            P[B[b_idx].idx] = b_idx;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            sb.append(P[i]).append(' ');
        }

        System.out.println(sb.toString());
    }
}