import java.util.Arrays;
import java.util.Scanner;

public class P_20291 {

    static int N;
    static String[] arr;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        arr = new String[N];
        for (int i = 0; i < N; i++) {
            String sibar = sc.next();
            arr[i] = sibar.split("\\.")[1];
        }
        Arrays.sort(arr);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N;) {
            String ext = arr[i];
            int j = i + 1;
            int cnt = 1;
            while (j < N && arr[j].equals(ext)) {
                cnt++;
                j++;
            }
            sb.append(ext).append(" ").append(cnt).append("\n");
            i = j;
        }

        System.out.println(sb.toString());
    }
}