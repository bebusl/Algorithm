import java.util.Arrays;
import java.util.Scanner;

public class P_10825 {

    static class Score implements Comparable<Score> {
        public String name;
        public int korean, english, math;

        @Override
        public int compareTo(Score o) {
            if (korean != o.korean)
                return o.korean - korean;
            if (english != o.english)
                return english - o.english;
            if (math != o.math)
                return o.math - math;
            return name.compareTo(o.name);
        }
    }

    static int N;
    static Score[] scores;

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            N = sc.nextInt();
            scores = new Score[N];
            for (int i = 0; i < N; i++) {
                scores[i] = new Score();
                scores[i].name = sc.next();
                scores[i].korean = sc.nextInt();
                scores[i].english = sc.nextInt();
                scores[i].math = sc.nextInt();
            }
        }
        Arrays.sort(scores);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            sb.append(scores[i].name).append('\n');
        }
        System.out.println(sb.toString());
    }
}