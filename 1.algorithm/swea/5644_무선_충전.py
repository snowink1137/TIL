import sys

sys.stdin = open('5644_sample_input.txt', 'r')


def score(x, y):
    scores = [0] * BC_num
    for i in range(BC_num):
        if abs(y-(BC_list[i][1]-1)) + abs(x-(BC_list[i][0]-1)) <= BC_list[i][2]:
            scores[i] = BC_list[i][3]

    return scores


def max_score(scores1, scores2):
    result = 0
    if BC_num == 1:
        return max(scores1[0], scores2[0])

    for i in range(BC_num):
        for j in range(BC_num):
            if i == j:
                continue

            if scores1[i] + scores2[j] > result:
                result = scores1[i] + scores2[j]

    return result


T = int(input())
for test_case in range(1, T+1):
    result = 0
    M, BC_num = map(int, input().split())
    A_move = list(map(int, input().split()))
    B_move = list(map(int, input().split()))

    BC_list = [list(map(int, input().split())) for _ in range(BC_num)]

    A = [0, 0]
    B = [9, 9]
    result += max_score(score(A[0], A[1]), score(B[0], B[0]))

    for i in range(M):
        if A_move[i] == 0:
            pass
        elif A_move[i] == 1:
            A[1] -= 1
        elif A_move[i] == 2:
            A[0] += 1
        elif A_move[i] == 3:
            A[1] += 1
        elif A_move[i] == 4:
            A[0] -= 1

        if B_move[i] == 0:
            pass
        elif B_move[i] == 1:
            B[1] -= 1
        elif B_move[i] == 2:
            B[0] += 1
        elif B_move[i] == 3:
            B[1] += 1
        elif B_move[i] == 4:
            B[0] -= 1

        result += max_score(score(A[0], A[1]), score(B[0], B[1]))

    print('#{} {}'.format(test_case, result))
