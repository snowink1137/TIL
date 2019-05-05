# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    N = len(A)
    total = ((1 + (N)) * N) // 2
    A_total = sum(A)

    if A_total == total:
        check = set(A)
        if len(A) == len(set(A)):
            return 1
        else:
            return 0
    else:
        return 0
