def solution(n, weak, dist):
    answer = -1
    dist.reverse()

    interval = [weak[0]+n-weak[-1]]
    for i in range(len(weak)-1):
        interval.append(weak[i+1]-weak[i])

    interval.sort(reverse=True)
    interval.pop(0)

    for i in range(len(dist)):
        if sum(interval) <= sum(dist[:i+1]):
            answer = i + 1
            break
        else:
            interval.pop(0)

    return answer


n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]
print(solution(n, weak, dist))
