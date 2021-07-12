# 결과: https://app.codility.com/demo/results/training75JSFA-QVQ/

def solution(X, A):
    leaf = 0
    check_dict = dict()

    cnt = -1
    for a in A:
        cnt += 1
        if check_dict.get(a):
            continue

        check_dict[a] = True
        leaf += 1
        if leaf == X:
            return cnt

    return -1


print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))
