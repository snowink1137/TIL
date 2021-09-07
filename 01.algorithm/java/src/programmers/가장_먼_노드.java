package programmers;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.OptionalInt;
import java.util.PriorityQueue;
import java.util.Queue;

public class 가장_먼_노드 {

    public int solution(int n, int[][] edge) {
        int answer = 0;

        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int[] e : edge) {
            int n1 = e[0];
            int n2 = e[1];

            createGraph(graph, n1, n2);
            createGraph(graph, n2, n1);
        }

        int[] visit = new int[n + 1];
        answer = bfs(1, graph, visit);

        return answer;
    }

    private int bfs(int start, Map<Integer, List<Integer>> graph, int[] visit) {
        Queue<Integer> queue = new ArrayDeque<Integer>();
        queue.add(start);
        visit[start] = 1;

        while (!queue.isEmpty()) {
            Integer q = queue.poll();
            int depth = visit[q];

            for (int g : graph.get(q)) {
                if ((visit[g] <= depth + 1) && visit[g] != 0) {
                    continue;
                }

                queue.add(g);
                visit[g] = depth + 1;
            }
        }

        int maxDepth = Arrays.stream(visit).max().orElse(0);
        long count = Arrays.stream(visit).filter(x -> x == maxDepth).count();

        return (int) count;
    }

    private void createGraph(Map<Integer, List<Integer>> graph, int n1, int n2) {
        if (graph.get(n1) == null) {
            List nextList = new ArrayList();
            nextList.add(n2);
            graph.put(n1, nextList);
        } else {
            List<Integer> nextList = graph.get(n1);
            nextList.add(n2);
        }
    }

    public static void main(String[] args) {
        int n = 6;
        int[][] vertex = {{3, 6}, {4, 3}, {3, 2}, {1, 3}, {1, 2}, {2, 4}, {5, 2}};

        가장_먼_노드 target = new 가장_먼_노드();
        System.out.println(target.solution(n, vertex));
    }
}
