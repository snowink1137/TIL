def solution(n):
    answer = 0

    n_3 = ''
    while n:
        if n < 3:
            n_3 = str(n) + n_3
            break

        r = n % 3
        n = n // 3
        n_3 = str(r) + n_3

    n_3 = n_3[::-1]
    answer = int(n_3, 3)

    return answer


n = 45
print(solution(n))
