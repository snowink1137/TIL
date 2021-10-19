def solution(n):
    answer = n

    for d in range(2, n):
        if n % d == 1:
            answer = d
            break

    return answer