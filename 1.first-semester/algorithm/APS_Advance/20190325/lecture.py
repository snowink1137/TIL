# # 1. quicksort(Hoare-Patition 알고리즘)
# arr = []
#
#
# def quick_sort(l, r):
#     if l >= r:
#         return
#
#     # arr[l] = pivot.
#     i, j = l, r
#     while i < j:
#         while i <= r and arr[l] >= arr[i]:
#             i += 1
#
#         while arr[l] < arr[j]:
#             j -= 1
#
#         if i < j:
#             arr[i], arr[j] = arr[j], arr[i]
#
#     arr[l], arr[j] = arr[j], arr[l]
#     quick_sort(l, j-1)
#     quick_sort(j+1, r)


# 2. quicksort(Lomuto partition 알고리즘)
arr = []


def quick_sort(l, r):
    if l >= r:
        return

    i = l - 1
    for j in range(l, r):
        if arr[j] <= arr[r]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    i += 1
    arr[i], arr[j] = arr[j], arr[i]
    quick_sort(l, i-1)
    quick_sort(i+1, r)
