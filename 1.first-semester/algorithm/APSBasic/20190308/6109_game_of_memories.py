import sys

sys.stdin = open('6109.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N, S = input().split()
    N = int(N)

    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    lines = []
    new_lines = []
    if S == 'up':
        for j in range(N):
            line = []
            for i in range(N):
                element = matrix[i][j]
                if element != 0:
                    line.append(matrix[i][j])

            lines.append(line)

        for line in lines:
            new_line = []
            line_length = len(line)

            if line_length == 1:
                new_line.append(line[0])
                new_lines.append(new_line)
                continue

            for j in range(1, line_length):
                before = line[j-1]
                after = line[j]
                if before == after:
                    new_line.append(before + after)
                    line[j] = 0
                else:
                    if before != 0:
                        new_line.append(before)

                    if after != 0 and j == (line_length - 1):
                        new_line.append(after)

            new_lines.append(new_line)

        result = [[0] * N for _ in range(N)]
        for j in range(N):
            for i in range(len(new_lines[j])):
                result[i][j] = new_lines[j][i]

        print('#{}'.format(test_case))
        for i in range(len(result)):
            print(' '.join(map(str, result[i])))

    elif S == 'down':
        change_matrix = []
        for row in reversed(matrix):
            change_matrix.append(row)

        matrix = change_matrix

        for j in range(N):
            line = []
            for i in range(N):
                element = matrix[i][j]
                if element != 0:
                    line.append(matrix[i][j])

            lines.append(line)

        for line in lines:
            new_line = []
            line_length = len(line)

            if line_length == 1:
                new_line.append(line[0])
                new_lines.append(new_line)
                continue

            for j in range(1, line_length):
                before = line[j-1]
                after = line[j]
                if before == after:
                    new_line.append(before + after)
                    line[j] = 0
                else:
                    if before != 0:
                        new_line.append(before)

                    if after != 0 and j == (line_length - 1):
                        new_line.append(after)

            new_lines.append(new_line)

        result = [[0] * N for _ in range(N)]
        for j in range(N):
            for i in range(len(new_lines[j])):
                result[i][j] = new_lines[j][i]

        change_matrix = []
        for row in reversed(result):
            change_matrix.append(row)

        result = change_matrix

        print('#{}'.format(test_case))
        for i in range(len(result)):
            print(' '.join(map(str, result[i])))

    elif S == 'left':
        change_matrix = [[0]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                change_matrix[i][j] = matrix[j][i]

        matrix = change_matrix

        for j in range(N):
            line = []
            for i in range(N):
                element = matrix[i][j]
                if element != 0:
                    line.append(matrix[i][j])

            lines.append(line)

        for line in lines:
            new_line = []
            line_length = len(line)

            if line_length == 1:
                new_line.append(line[0])
                new_lines.append(new_line)
                continue

            for j in range(1, line_length):
                before = line[j-1]
                after = line[j]
                if before == after:
                    new_line.append(before + after)
                    line[j] = 0
                else:
                    if before != 0:
                        new_line.append(before)

                    if after != 0 and j == (line_length - 1):
                        new_line.append(after)

            new_lines.append(new_line)

        result = [[0] * N for _ in range(N)]
        for j in range(N):
            for i in range(len(new_lines[j])):
                result[i][j] = new_lines[j][i]

        change_matrix = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                change_matrix[i][j] = result[j][i]

        result = change_matrix

        print('#{}'.format(test_case))
        for i in range(len(result)):
            print(' '.join(map(str, result[i])))

    elif S == 'right':
        change_matrix = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                change_matrix[i][N-1-j] = matrix[i][j]

        temp_matrix = change_matrix

        change_matrix = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                change_matrix[j][N - 1 - i] = temp_matrix[i][j]

        matrix = change_matrix

        for j in range(N):
            line = []
            for i in range(N):
                element = matrix[i][j]
                if element != 0:
                    line.append(matrix[i][j])

            lines.append(line)

        for line in lines:
            new_line = []
            line_length = len(line)

            if line_length == 1:
                new_line.append(line[0])
                new_lines.append(new_line)
                continue

            for j in range(1, line_length):
                before = line[j-1]
                after = line[j]
                if before == after:
                    new_line.append(before + after)
                    line[j] = 0
                else:
                    if before != 0:
                        new_line.append(before)

                    if after != 0 and j == (line_length - 1):
                        new_line.append(after)

            new_lines.append(new_line)

        result = [[0] * N for _ in range(N)]
        for j in range(N):
            for i in range(len(new_lines[j])):
                result[i][j] = new_lines[j][i]

        change_matrix = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                change_matrix[i][N - 1 - j] = result[i][j]

        temp_matrix = change_matrix

        change_matrix = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                change_matrix[j][N - 1 - i] = temp_matrix[i][j]

        result = change_matrix

        print('#{}'.format(test_case))
        for i in range(len(result)):
            print(' '.join(map(str, result[i])))

