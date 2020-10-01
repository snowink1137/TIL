from collections import deque


def solution(progresses, speeds):
    answer = []
    q_progresses = deque(progresses)
    q_speeds = deque(speeds)

    while q_progresses:
        first_progress = q_progresses.popleft()
        first_speed = q_speeds.popleft()

        cnt = 0
        while first_progress < 100:
            first_progress += first_speed
            cnt += 1

        while cnt:
            for i in range(len(q_progresses)):
                q_progresses[i] += q_speeds[i]

            cnt -= 1

        cnt = 1
        for p in q_progresses:
            if p < 100:
                break
            cnt += 1

        for _ in range(cnt-1):
            q_progresses.popleft()
            q_speeds.popleft()

        answer.append(cnt)

    return answer


progresses = [90]
speeds = [1]
print(solution(progresses, speeds))
