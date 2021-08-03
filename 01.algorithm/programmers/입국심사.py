def solution(n, times):
    answer = 0
    left = 1
    right = max(times) * n

    while left <= right:
        mid = (left + right) // 2
        number = 0

        for time in times:
            number += mid // time

            if number >= n:
                break

        if number >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer


n = 6
times = [7, 10]
print(solution(n, times))
