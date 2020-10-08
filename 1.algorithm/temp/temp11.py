def divide(i, j, n):
    result = [
        [[i + 0, i + n // 2 - 1], [j + 0, j + n // 2 - 1]],
        [[i + n // 2, i + n - 1], [j + 0, j + n // 2 - 1]],
        [[i + 0, i + n // 2 - 1], [j + n // 2, j + n - 1]],
        [[i + n // 2, i + n - 1], [j + n // 2, j + n - 1]],
    ]

    return result


def check(i_list, j_list, arr):
    num = arr[i_list[0]][j_list[0]]
    for i in i_list:
        for j in j_list:
            if num != arr[i][j]:
                return False

    return True


def solution(arr):
    temp = sum(map(sum, arr))
    size = len(arr)
    answer = [size**2 - temp, temp]

    while size:
        size


    return answer


arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
print(solution(arr))
