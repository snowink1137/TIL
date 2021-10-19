def solution(n, left, right):
    answer = []

    left_d, left_r = divmod(left, n)
    right_d, right_r = divmod(right, n)

    if right_d - left_d > 1:
        for j in range(left_r, n):
            answer.append(max(j, left_d) + 1)

        for i in range(left_d+1, right_d):
            for j in range(n):
                answer.append(max(i, j) + 1)

        for j in range(right_r+1):
            answer.append(max(j, right_d) + 1)
    elif right_d - left_d == 1:
        for j in range(left_r, n):
            answer.append(max(j, left_d) + 1)

        for j in range(right_r+1):
            answer.append(max(j, right_d) + 1)
    else:
        for j in range(left_r, right_r + 1):
            answer.append(max(left_d, j) + 1)

    return answer


n = 3
left = 5
right = 8
print(solution(n, left, right))
