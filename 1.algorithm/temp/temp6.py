from collections import deque


def solution(T,R,k):
    answer = 0
    T.insert(0, 0)

    answer_list = [0 for _ in range(len(T))]
    previous_list = [[] for _ in range(len(T))]

    for r in R:
        previous_list[r[1]].append(r[0])

    answer_list[k] = T[k]
    queue = deque()
    queue.append(k)
    while queue:
        next = queue.popleft()
        for n in previous_list[next]:
            if answer_list[n] > answer_list[next] + T[n]:
                queue.append(n)
                continue

            answer_list[n] = answer_list[next] + T[n]
            queue.append(n)

    answer = max(answer_list)
    return answer


T = [5,8,3,7,10,5,4]
R = [[1,2],[2,4],[1,4],[6,5],[3,5],[4,6]]
k = 5
print(solution(T, R, k))
# 35
