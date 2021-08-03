import heapq


def solution(operations):
    heap = []

    for operation in operations:
        split_operation = operation.split()

        if split_operation[0] == 'I':
            heapq.heappush(heap, int(split_operation[1]))
        else:
            if not len(heap):
                continue

            if split_operation[1] == '1':
                heap.remove(max(heap))
            else:
                heapq.heappop(heap)

    if len(heap):
        return [max(heap), min(heap)]

    return [0, 0]


operations = ['I 16', 'D 1']
print(solution(operations))

