def solution(A: list):
    right = 0
    result = -1

    while right < len(A):
        temp = 0
        check = False
        while right < len(A) and A[right] >= 0:
            check = True
            temp += A[right]
            right += 1

        if check and temp > result:
            result = temp

        right += 1

    return result


A = [1, 2, -3, 4, 5, -6]
print(solution(A))
