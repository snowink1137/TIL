# 결과: https://app.codility.com/demo/results/training4DDHM6-ZKX/

def solution(A):
    A = sorted(A)

    if A[0] > 1 or A[-1] < 1:
        return 1

    for i in range(len(A) - 1):
        temp = A[i] if A[i] >= 0 else 0

        if A[i + 1] - temp > 1:
            return temp + 1
    else:
        return A[-1] + 1


A = [-10001, 10002]
print(solution(A))
