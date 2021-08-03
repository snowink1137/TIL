import heapq as hq


def solution(jobs):
    answer = 0
    wait = []
    length = len(jobs)
    last = -1
    now = 0

    cnt = 0
    while cnt < length:
        for job in jobs:
            if last < job[0] <= now:  # 요청 시간이 도래한 것만 대기열에 추가
                answer += now - job[0]  # 대기열 들어가기 전까지의 지연 시간
                hq.heappush(wait, job[1])  # 대기열에 있는 것들 중 요청시간이 짧은 것으로 우선 순위 매기기

        if len(wait) > 0:
            answer += len(wait) * wait[0]  # 대기열 들어가고 나서 다른 요청 처리때문에 걸리는 지연 시간

            last = now
            now += hq.heappop(wait)
            cnt += 1
        else:
            now += 1

    return answer // length


jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))
