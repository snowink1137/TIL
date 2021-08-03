def solution(rows, columns, queries):
    answer = []
    matrix = []
    cnt = 0
    for _ in range(rows):
        matrix.append([i for i in range(cnt+1, cnt+columns+1)])
        cnt += columns

    for query in queries:
        x1, y1, x2, y2 = query[0]-1, query[1]-1, query[2]-1, query[3]-1
        temp = matrix[x1][y1]
        min_value = temp

        for i in range(0, x2-x1):
            matrix[x1+i][y1] = matrix[x1+i+1][y1]
            min_value = min(min_value, matrix[x1+i][y1])

        for i in range(0, y2-y1):
            matrix[x2][y1+i] = matrix[x2][y1+i+1]
            min_value = min(min_value, matrix[x2][y1+i])

        for i in range(0, x2-x1):
            matrix[x2-i][y2] = matrix[x2-i-1][y2]
            min_value = min(min_value, matrix[x2-i][y2])

        for i in range(0, y2-y1):
            matrix[x1][y2-i] = matrix[x1][y2-i-1]
            min_value = min(min_value, matrix[x1][y2-i])

        min_value = min(min_value, matrix[x1][y1+1])
        matrix[x1][y1+1] = temp

        answer.append(min_value)

    return answer


rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(rows, columns, queries))
