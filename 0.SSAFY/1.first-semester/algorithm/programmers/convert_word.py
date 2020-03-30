def solution(begin, target, words):
    answer = 0
    queue = []
    visit = [0 for i in range(len(words))]
    n = len(begin)

    if target not in words:
        return answer

    for i in range(len(words)):
        cnt = 0
        for j in range(n):
            if begin[j] == words[i][j]:
                cnt += 1

        if cnt == n - 1:
            queue.append(i)
            visit[i] = 1

    while len(queue):
        q = queue.pop()
        if words[q] == target:
            answer = visit[q]
            break

        for i in range(len(words)):
            if visit[i]:
                continue

            cnt = 0
            for j in range(n):
                if words[i][j] == words[q][j]:
                    cnt += 1

            if cnt == n - 1:
                queue.append(i)
                visit[i] = visit[q] + 1

    return answer


print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
