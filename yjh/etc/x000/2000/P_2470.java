import java.io.*;
import java.util.*;

public class P_2470 {
    static FastReader s = new FastReader();

    static int N;
    static int[] arr;

    static int lower_bound(int[] arr, int L, int R, int value) {
        int result = R + 1;
        while (L <= R) {
            int mid = (L + R) / 2;
            if (arr[mid] >= value) {
                result = mid;
                R = mid - 1;
            } else if (arr[mid] < value) {
                L = mid + 1;
            }
        }
        return result;
    }

    public static void main(String[] args) {
        N = s.nextInt();
        arr = new int[N + 1];
        for (int i = 1; i <= N; i++)
            arr[i] = s.nextInt();

        Arrays.sort(arr, 1, N + 1);

        int sum = Integer.MAX_VALUE;
        int[] answer = new int[2];
        for (int i = 1; i < N; i++) {
            int idx = lower_bound(arr, i + 1, N, -arr[i]);
            int cur_sum;
            if (idx <= N) {
                cur_sum = Math.abs(arr[i] + arr[idx]);
                if (sum > cur_sum) {
                    sum = cur_sum;
                    answer[0] = arr[i];
                    answer[1] = arr[idx];
                }
            }
            if (i < idx - 1) {
                cur_sum = Math.abs(arr[i] + arr[idx - 1]);
                if (sum > cur_sum) {
                    sum = cur_sum;
                    answer[0] = arr[i];
                    answer[1] = arr[idx - 1];
                }
            }
        }
        System.out.println(answer[0] + " " + answer[1]);

    }

    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        public FastReader(String s) throws FileNotFoundException {
            br = new BufferedReader(new FileReader(new File(s)));
        }

        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        long nextLong() {
            return Long.parseLong(next());
        }

        double nextDouble() {
            return Double.parseDouble(next());
        }

        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
}
