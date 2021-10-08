def solution(key, lock):
    answer = False
    size_key = len(key)
    size_lock = len(lock)

    test_matrix = [[0 for _ in range(size_lock+size_key*2)] for _ in range(size_lock+size_key*2)]
    for i in range(size_lock):
        for j in range(size_lock):
            test_matrix[size_key+i][size_key+j] = lock[i][j]

    test_key = []
    for k in key:
        test_key.append(k[:])

    for i in range(0, size_key+size_lock):
        for j in range(0, size_key+size_lock):
            for _ in range(4):
                test_key = rotate_90(test_key)
                stage(test_matrix, test_key, i, j, size_key)

                if test(test_matrix, size_key, size_lock):
                    return True

                unstage(test_key, test_matrix, i, j, size_key)

    return answer


def rotate_90(matrix):
    return list(zip(*matrix[::-1]))


def stage(test_matrix, test_key, start_i, start_j, size_key):
    for i in range(size_key):
        for j in range(size_key):
            test_matrix[start_i+i][start_j+j] += test_key[i][j]

    return


def unstage(test_key, test_matrix, start_i, start_j, size_key):
    for i in range(size_key):
        for j in range(size_key):
            test_matrix[start_i+i][start_j+j] -= test_key[i][j]

    return


def test(test_matrix, size_key, size_lock):
    result = True

    for i in range(size_key, size_key+size_lock):
        for j in range(size_key, size_key+size_lock):
            if test_matrix[i][j] != 1:
                result = False

    return result


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))
