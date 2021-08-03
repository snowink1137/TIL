# from queue import PriorityQueue
#
#
# def solution(scoville, K):
#     answer = 0
#     pqueue = PriorityQueue(len(scoville))
#
#     for s in scoville:
#         pqueue.put(s)
#
#     while True:
#         if pqueue.qsize() == 1:
#             first = pqueue.get()
#             if first < K:
#                 return -1
#             else:
#                 return answer
#
#         first = pqueue.get()
#         if first >= K:
#             return answer
#
#         second = pqueue.get()
#
#         pqueue.put(first+second*2)
#         answer += 1
#
#     return answer


import heapq


def solution(scoville, K):
    answer = 0
    pqueue = []

    for s in scoville:
        heapq.heappush(pqueue, s)

    while True:
        if len(pqueue) == 1:
            first = heapq.heappop(pqueue)
            if first < K:
                return -1
            else:
                return answer

        first = heapq.heappop(pqueue)
        if first >= K:
            return answer

        second = heapq.heappop(pqueue)

        heapq.heappush(pqueue, first+second*2)
        answer += 1

    return answer


scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))
