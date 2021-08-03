from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_queue = deque([0 for _ in range(bridge_length)])
    truck_queue = deque(truck_weights)
    bridge_weight = 0

    while bridge_queue:
        bridge_weight -= bridge_queue.pop()
        if truck_queue:
            if bridge_weight + truck_queue[0] <= weight:
                next = truck_queue.popleft()
                bridge_queue.appendleft(next)
                bridge_weight += next
            else:
                bridge_queue.appendleft(0)

        answer += 1

    return answer


bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]
print(solution(bridge_length, weight, truck_weights))
