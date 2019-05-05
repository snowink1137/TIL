# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    result = -1
    visit = [False] * (X + 1)
    visit[A[0]] = True

    for i in range(A[0]):
        visit[i] = True

    total = sum(visit)
    length = len(visit)

    if len(A) > 1:
        cnt = 1
        for a in A[1:]:
            if not visit[a]:
                visit[a] = True
                total += 1
                if total == length:
                    return cnt

            cnt += 1

    else:
        if total == length:
            return 0

    return result
