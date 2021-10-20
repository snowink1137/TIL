package goorm;

import java.util.*;
import java.util.stream.Collectors;

public class 행렬의_영역 {

    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};

    private static void solution(int sizeOfMatrix, int[][] matrix) {
        int cnt = 0;
        List<Integer> size = new ArrayList();
        int[][] visit = new int[matrix.length][matrix.length];

        for (int i = 0; i < sizeOfMatrix; i++) {
            for (int j = 0; j < sizeOfMatrix; j++) {
                if (matrix[i][j] == 1 && visit[i][j] != 1) {
                    cnt++;
                    size.add(bfs(i, j, matrix, visit));
                }
            }
        }
        System.out.println(cnt);
        String result = size.stream()
                .sorted()
                .map(n -> String.valueOf(n))
                .collect(Collectors.joining(" "));
        System.out.println(result);
    }

    private static int bfs(int i, int j, int[][] matrix, int[][] visit) {
        int cnt = 0;
        Queue<int[]> queue = new ArrayDeque();
        queue.add(new int[]{i, j});
        visit[i][j] = 1;
        cnt += 1;

        while (!queue.isEmpty()) {
            int[] q = queue.poll();
            int x = q[0];
            int y = q[1];

            for (int k = 0; k < 4; k++) {
                int x1 = x + dx[k];
                int y1 = y + dy[k];

                if (x1 < 0 || x1 > matrix.length-1 || y1 < 0 || y1 > matrix.length-1 || matrix[x1][y1] == 0 || visit[x1][y1] != 0) {
                    continue;
                }

                queue.add(new int[]{x1, y1});
                visit[x1][y1] = 1;
                cnt += 1;
            }
        }

        return cnt;
    }

    private static class InputData {
        int sizeOfMatrix;
        int[][] matrix;

    }

    private static InputData processStdin() {
        InputData inputData = new InputData();

        try (Scanner scanner = new Scanner(System.in)) {
            inputData.sizeOfMatrix = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));
            inputData.matrix = new int[inputData.sizeOfMatrix][inputData.sizeOfMatrix];

            for (int i = 0; i < inputData.sizeOfMatrix; i++) {
                String[] buf = scanner.nextLine().trim().replaceAll("\\s+", " ").split(" ");
                for (int j = 0; j < inputData.sizeOfMatrix; j++) {
                    inputData.matrix[i][j] = Integer.parseInt(buf[j]);
                }
            }
        } catch (Exception e) {
            throw e;
        }

        return inputData;
    }

    public static void main(String[] args) throws Exception {
        InputData inputData = processStdin();
        solution(inputData.sizeOfMatrix, inputData.matrix);
    }
}
