import java.io.*;
import java.util.*;

public class P_11725 {
    static int N, cur;
    static ArrayList<Integer>[] adj;
    static boolean[] visited;
    static int[] parents;
    static StringBuilder sb;

    static void bfs(int start) {
        Queue<Integer> q = new LinkedList<>();
        q.add(start);
        visited[start] = true;

        while (!q.isEmpty()) {
            cur = q.poll();

            for (int child : adj[cur]) {
                if (visited[child])
                    continue;

                parents[child] = cur;
                visited[child] = true;
                q.add(child);
            }
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        adj = new ArrayList[N + 1];
        visited = new boolean[N + 1];
        parents = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            adj[i] = new ArrayList<Integer>();
        }
        for (int i = 1; i < N; i++) {
            String[] inputs = br.readLine().split(" ");
            int u = Integer.parseInt(inputs[0]);
            int v = Integer.parseInt(inputs[1]);
            adj[u].add(v);
            adj[v].add(u);
        }

        bfs(1);

        sb = new StringBuilder();
        for (int i = 2; i <= N; i++) {
            sb.append(parents[i]).append("\n");
        }
        System.out.println(sb);
    }
}
