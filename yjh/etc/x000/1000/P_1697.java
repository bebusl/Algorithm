import java.io.*;
import java.util.*;

public class P_1697 {
    static int N, K, arrSize, cur, temp;
    static int[] dist;

    static void bfs() {
        Queue<Integer> q = new LinkedList<>();
        q.add(N);
        dist[N] = 0;

        while (!q.isEmpty()) {
            cur = q.poll();

            temp = cur + 1;
            if (0 <= temp && temp <= 100000 && dist[temp] == -1) {
                dist[temp] = dist[cur] + 1;
                q.add(temp);
            }
            temp = cur - 1;
            if (0 <= temp && temp <= 100000 && dist[temp] == -1) {
                dist[temp] = dist[cur] + 1;
                q.add(temp);
            }
            temp = cur * 2;
            if (0 <= temp && temp <= 100000 && dist[temp] == -1) {
                dist[temp] = dist[cur] + 1;
                q.add(temp);
            }

        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = br.readLine().split(" ");
        N = Integer.parseInt(inputs[0]);
        K = Integer.parseInt(inputs[1]);

        dist = new int[100001];
        for (int i = 0; i <= 100000; i++)
            dist[i] = -1;

        bfs();

        System.out.println(dist[K]);
    }

}
