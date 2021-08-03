def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)
    left = 0
    right = distance * 2

    while left <= right:
        temp_answer = distance
        mid = (left + right) // 2
        before = 0

        cnt = 0
        for i in range(len(rocks)):
            diff = rocks[i] - before
            if diff < mid:
                cnt += 1
            else:
                if diff < temp_answer:
                    temp_answer = diff

                before = rocks[i]

            if cnt > n:
                break

        if cnt > n:
            right = mid - 1
        else:
            answer = temp_answer
            left = mid + 1

    return answer


distance = 25
rocks = [2, 14, 11, 21, 17]
n = 2
print(solution(distance, rocks, n))
