import heapq as hq


def solution(n, times):
    answer = 0
    times_heap = []

    if n < len(times):
        times.sort()
        return times[n-1]

    for time in times:
        hq.heappush(times_heap, [time*2, time])

    n -= len(times)

    for _ in range(n):
        temp = hq.heappop(times_heap)
        temp[0] += temp[1]

        hq.heappush(times_heap, temp)

    result_temp = hq.nlargest(len(times), times_heap)

    return result_temp[0][0] - result_temp[0][1]


n = 6
times = [7, 10]
print(solution(n, times))
