from collections import deque


def solution(priorities, location):
    answer = 0
    priorities_queue = deque([(i, v) for i, v in enumerate(priorities)])

    while priorities_queue:
        q = priorities_queue.popleft()

        if priorities_queue and max(priorities_queue, key=lambda x: x[1])[1] > q[1]:
            priorities_queue.append(q)
        else:
            answer += 1
            if q[0] == location:
                break

    return answer


priorities = [2, 1, 3, 2]
location = 2
print(solution(priorities, location))
