package programmers;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class 가장_먼_노드 {

    public int solution(int n, int[][] edge) {
        int answer = 0;

        Map<Integer, List> graph = new HashMap<>();


        return answer;
    }

    public static void main(String[] args) {
        int n = 6;
        int[][] vertex = {{3, 6}, {4, 3}, {3, 2}, {1, 3}, {1, 2}, {2, 4}, {5, 2}};

        가장_먼_노드 target = new 가장_먼_노드();
        System.out.println(target.solution(n, vertex));
    }
}
