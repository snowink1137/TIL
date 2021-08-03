# 결과1: https://app.codility.com/demo/results/trainingHPG585-CNU/
# 결과2: https://app.codility.com/demo/results/trainingG5HACT-4HA/

def solution(N, A):
    result = [0 for _ in range(N)]

    current_max_number = 0
    last_max_number = 0
    for a in A:
        if a <= N:
            if result[a-1] < last_max_number:
                result[a-1] = last_max_number + 1
            else:
                result[a-1] += 1

            if current_max_number < result[a-1]:
                current_max_number = result[a-1]
        else:
            last_max_number = current_max_number

    for i in range(len(result)):
        if result[i] < last_max_number:
            result[i] = last_max_number

    return result


N = 5
A = [3, 4, 4, 6, 1, 4, 4]
print(solution(N, A))
