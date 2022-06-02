import java.io.*;
import java.util.*;

public class P_3055 {
    static int R, C;
    static char[][] map;
    static int[][] dist_water, dist;
    static int[][] dir = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };

    public static void bfs_water() {
        Queue<Integer> q = new LinkedList<>();

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (map[i][j] == '*') {
                    q.add(i);
                    q.add(j);
                    dist_water[i][j] = 0;
                } else {
                    dist_water[i][j] = -1;
                }
            }
        }

        while (!q.isEmpty()) {
            int cur_r = q.poll();
            int cur_c = q.poll();

            for (int i = 0; i < 4; i++) {
                int temp_r = cur_r + dir[i][0];
                int temp_c = cur_c + dir[i][1];
                if (0 <= temp_r && temp_r < R && 0 <= temp_c && temp_c < C && dist_water[temp_r][temp_c] == -1) {
                    if (map[temp_r][temp_c] != '.')
                        continue;

                    dist_water[temp_r][temp_c] = dist_water[cur_r][cur_c] + 1;
                    q.add(temp_r);
                    q.add(temp_c);
                }
            }
        }
    }

    static void bfs() {
        Queue<Integer> q = new LinkedList<>();

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (map[i][j] == 'S') {
                    q.add(i);
                    q.add(j);
                    dist[i][j] = 0;
                } else {
                    dist[i][j] = -1;
                }
            }
        }

        while (!q.isEmpty()) {
            int cur_r = q.poll();
            int cur_c = q.poll();

            for (int i = 0; i < 4; i++) {
                int temp_r = cur_r + dir[i][0];
                int temp_c = cur_c + dir[i][1];
                if (0 <= temp_r && temp_r < R && 0 <= temp_c && temp_c < C && dist[temp_r][temp_c] == -1) {
                    int limit = dist_water[temp_r][temp_c];
                    if (map[temp_r][temp_c] != '.' && map[temp_r][temp_c] != 'D')
                        continue;
                    if (limit != -1 && dist[cur_r][cur_c] + 1 >= limit)
                        continue;
                    dist[temp_r][temp_c] = dist[cur_r][cur_c] + 1;
                    q.add(temp_r);
                    q.add(temp_c);
                }
            }
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = br.readLine().split(" ");
        R = Integer.parseInt(inputs[0]);
        C = Integer.parseInt(inputs[1]);
        map = new char[R][C];
        dist_water = new int[R][C];
        dist = new int[R][C];
        for (int i = 0; i < R; i++) {
            map[i] = br.readLine().toCharArray();
        }

        bfs_water();

        bfs();

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (map[i][j] == 'D') {
                    if (dist[i][j] == -1)
                        System.out.println("KAKTUS");
                    else
                        System.out.println(dist[i][j]);
                    break;
                }
            }
        }

    }
}
