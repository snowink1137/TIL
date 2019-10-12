answer = 0


def dfs(numbers, start, limit, score, target):
    global answer

    if start == limit:
        if score == target:
            answer += 1

        return

    dfs(numbers, start+1, limit, score+numbers[start], target)
    dfs(numbers, start+1, limit, score-numbers[start], target)


def solution(numbers, target):
    global answer
    limit = len(numbers)

    dfs(numbers, 0, limit, 0, target)

    return answer


print(solution([1, 1, 1, 1, 1], 3))
