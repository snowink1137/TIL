def solution(A: list):
    target = int((sum(A) / len(A)) + 0.5)
    result = 0
    for a in A:
        result += abs(a - target)

    return result


A = [3, 3, 3]
print(solution(A))
