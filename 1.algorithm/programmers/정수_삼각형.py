def solution(triangle):
    answer = 0
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            first = j - 1
            second = j

            if 0 <= first < len(triangle[i-1]) and 0 <= second < len(triangle[i-1]):
                triangle[i][j] = max(triangle[i][j]+triangle[i-1][first], triangle[i][j]+triangle[i-1][second])
            elif first < 0:
                triangle[i][j] = triangle[i][j] + triangle[i-1][second]
            elif second > len(triangle[i-1]) - 1:
                triangle[i][j] = triangle[i][j] + triangle[i-1][first]

    answer = max(triangle[len(triangle)-1])

    return answer


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))
