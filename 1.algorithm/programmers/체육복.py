def solution(n, lost, reserve):
    answer = 0
    reserve_list = [False for _ in range(n+1)]
    lost_list = [False for _ in range(n+1)]

    lost.sort()
    reserve.sort()

    for l in lost:
        lost_list[l] = True

    for r in reserve:
        if lost_list[r]:
            lost_list[r] = False
            continue

        reserve_list[r] = True

    for l in lost:
        if reserve_list[l-1]:
            reserve_list[l-1] = False
            lost_list[l] = False
            continue

        if l == n:
            continue

        if reserve_list[l+1]:
            reserve_list[l+1] = False
            lost_list[l] = False

    answer = n - sum(lost_list)
    return answer


n = 5
lost = [1, 2, 3]
reserve = [3]
print(solution(n, lost, reserve))
