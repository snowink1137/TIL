# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    from collections import deque

    arr = deque(A)
    arr.rotate(K)

    return arr

print(solution([1,2,3], 1))
