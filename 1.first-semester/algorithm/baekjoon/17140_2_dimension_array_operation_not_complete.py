import sys

sys.stdin = open('17140.txt', 'r')


def operate():
    length = 0
    for row in matrix:
        temp_row = []
        for i in range(1, max(row)+1):
            row_cnt = row.count(i)
            if row_cnt:
                temp_row.append((i, row_cnt))

        temp_length = len(temp_row) * 2
        if temp_length > length:
            length = temp_length

        temp_row.sort(key=lambda x: (x[1], x[0]))
        temp_matrix.append([val for tup in temp_row for val in tup])

    for temp_row in temp_matrix:
        difference = length - len(temp_row)

        if difference:
            temp_row.extend([0]*difference)


r, c, k = map(int, input().split())
r -= 1
c -= 1
matrix = [list(map(int, input().split())) for _ in range(3)]

cnt = 0
result = -1
while cnt <= 100:
    if matrix[r][c] == k:
        result = cnt
        break

    R = len(matrix)
    C = len(matrix[0])

    if R >= C:
        temp_matrix = []
        operate()
        matrix = [row[:] for row in temp_matrix]
    else:
        temp_matrix = []
        reversed_matrix = [[0 for _ in range(R)] for _ in range(C)]
        for i in range(R):
            for j in range(C):
                reversed_matrix[j][i] = matrix[i][j]

        matrix = [row[:] for row in reversed_matrix]

        operate()

        reversed_matrix = [[0 for _ in range(C)] for _ in range(R)]
        for i in range(R):
            for j in range(C):
                reversed_matrix[j][i] = matrix[i][j]

        matrix = [row[:] for row in temp_matrix]

    cnt += 1


print(result)
