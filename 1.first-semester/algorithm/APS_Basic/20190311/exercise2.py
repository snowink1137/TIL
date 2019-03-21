arr = [69, 10, 30, 2, 16, 8, 31, 22]


def merge_sort(m):
    if len(m) <= 1:
        return m

    # 1. DIVIDE 부분
    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]

    # 리스트의 크기가 1이 될 때까지 merge_sort 재귀 호출
    left = merge_sort(left)
    right = merge_sort(right)

    # 2. CONQUER 부분
    return merge(left, right)


def merge(left, right):
    result = []

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if len(left) > 0:
        result.extend(left)
    if len(right) > 0:
        result.extend(right)

    return result


arr_sorted = merge_sort(arr)
print(arr_sorted)
